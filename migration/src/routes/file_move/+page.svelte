<script lang="ts">
    import type {FilePath} from "./common"
    import "../pages.scss";
    import Entry from "./entry.svelte";

    let filePath: FilePath = {
        current_path: "",
        new_path: "",
        name: ""
    };

    let filePaths: FilePath[] = []

    function onAdd() {
        if (filePath.name === "") {
            delete filePath.name;
        }
        filePaths.push(filePath);
        filePaths = filePaths;
        filePath = {
            current_path: "",
            new_path: "",
            name: ""
        };
    }

    function onSubmit() {
        let response = fetch("/api/file_move_paths", {
            method: "PUT",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(filePaths)
        });
        filePaths = [];
    }
</script>

<div style="margin-left: 10px;">
    <h1 style="color: #eceff4;">File Move Paths</h1>
    <div class="m-2">
        <Entry bind:entry={filePath} type="selected"/>
        <div class="flex w-72">
            <button type="button" class="w-full button left selected" on:click={onAdd}>
                Add
            </button>
            <button type="button" class="w-full button right selected" on:click={onSubmit}>
                Submit
            </button>
        </div>
    </div>
    {#each filePaths as entry}
    <div class="m-2">
        <Entry bind:entry={entry} type=""/>
    </div>
    {/each}
</div>