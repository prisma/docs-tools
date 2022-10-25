<script lang="ts">
    import type {FilePath} from "./common"
    import "../pages.scss";
    import Entry from "./entry.svelte";
    import {database} from "../../global";

    let filePath: FilePath = {
        current_path: "",
        redirect: "",
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
            redirect: "",
            name: ""
        };
    }

    function onSubmit() {
        let response = fetch("/api/file_delete_paths", {
            method: "PUT",
            headers: {
                ...((database != "") && {"database": database}),
                "Content-Type": "application/json"
            },
            body: JSON.stringify(filePaths)
        });
        filePaths = [];
    }
</script>

<div style="margin-left: 10px;">
    <h1 style="color: #eceff4;">File Delete Paths</h1>
    <div class="m-2">
        <Entry bind:entry={filePath} type="selected"/>
        <div class="flex w-96">
            <button type="button" class="w-full button selected" on:click={onAdd}>
                Add
            </button>
        </div>
        {#each filePaths as entry, index}
            <div class={"flex-auto h-7 box single"}>{index}:</div>
            <Entry bind:entry={entry} type=""/>
        {/each}
        <div class={"flex-auto h-2 box single"}></div>
        <div class="flex w-96">
            <button type="button" class="w-full button" on:click={onSubmit}>
                Submit
            </button>
        </div>
    </div>
</div>
