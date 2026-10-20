import { app } from "../../scripts/app.js";

app.registerExtension({
    name: "TextLoadFileCustom.DynamicDropdown",
    async beforeRegisterNodeDef(nodeType, nodeData, app) {
        if (nodeData.name !== "TextLoadFileAdvanced") return;

        const onNodeCreated = nodeType.prototype.onNodeCreated;
        nodeType.prototype.onNodeCreated = function () {
            const r = onNodeCreated?.apply(this, arguments);

            const folderWidget = this.widgets.find((w) => w.name === "folder_path");
            const fileWidget = this.widgets.find((w) => w.name === "text_file");
            if (!folderWidget || !fileWidget) return r;

            const refreshOptions = async () => {
                const folder = (folderWidget.value || "").trim();
                if (!folder) return;
                try {
                    const resp = await fetch(
                        `/textloadfilecustom/list_txt?folder=${encodeURIComponent(folder)}`
                    );
                    const data = await resp.json();
                    if (!data || !Array.isArray(data.files)) return;

                    const prev = fileWidget.value;
                    fileWidget.options.values = data.files;
                    if (data.files.length > 0 && !data.files.includes(prev)) {
                        fileWidget.value = data.files[0];
                    }
                    // notify the combo widget so the dropdown re-renders
                    if (fileWidget.callback) {
                        fileWidget.callback(fileWidget.value);
                    }
                    app.graph.setDirtyCanvas(true);
                } catch (e) {
                    console.error("TextLoadFileCustom refresh error", e);
                }
            };

            const origCallback = folderWidget.callback;
            folderWidget.callback = function (...args) {
                if (origCallback) origCallback.apply(this, args);
                refreshOptions();
            };

            // when loading a workflow that already has folder_path set,
            // refresh the dropdown to match that folder
            setTimeout(refreshOptions, 300);

            return r;
        };
    },
});
