<script lang="ts">
    import "../pages.scss";
    import Entries from "../entries.svelte";

    interface FileDeletePath {
        [key: string]: string | undefined;
        path: string;
        redirect?: string;
        name?: string;
    }

    interface FileDeletePaths {
        data: FileDeletePath[];
    }

    let fileDeletePath: FileDeletePath = {
        path: "",
        redirect: "",
        name: ""
    };

    let fileDeletePaths: FileDeletePaths = {
        data: []
    };

    function onAdd() {
        if (fileDeletePath.name === "") {
            delete fileDeletePath.name;
        }
        if (fileDeletePath.redirect === "") {
            delete fileDeletePath.redirect;
        }
        fileDeletePaths.data.push(fileDeletePath);
        fileDeletePaths = fileDeletePaths;
        fileDeletePath = {
            path: "",
            redirect: "",
            name: ""
        };
    }

    function onSubmit() {
        let response = fetch("/api/file_move_paths", {
            method: "PUT",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(fileDeletePaths)
        });
        fileDeletePaths.data = [];
    }
</script>

<div style="margin-left: 10px;">
    <h1 style="color: #eceff4;">File Delete Paths</h1>
    <input type="text" class="inner-each top selected" placeholder="Name*" bind:value={fileDeletePath.name}>
    <input type="text" class="inner-each middle selected" placeholder="Current Path" bind:value={fileDeletePath.path}>
    <input type="text" class="inner-each middle selected" placeholder="Redirect*" bind:value={fileDeletePath.redirect}>
    <div style="display: flex; flex-direction: row; width: 200px">
        <button type="button" class="button left selected" on:click={onAdd}>Add</button>
        <button type="button" class="button right selected" on:click={onSubmit}>Submit</button>
    </div>
</div>

<div style="margin-left: 10px;">
    <Entries entries={fileDeletePaths} items={["name", "path", "redirect"]}/>
</div>