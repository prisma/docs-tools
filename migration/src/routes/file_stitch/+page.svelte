<script lang="ts">
    import type {BodyPart, FilePath} from "./common";
    import "../pages.scss";
    import Entry from "./entry.svelte"

    let filePaths: FilePath[] = [];

    let filePath: FilePath = {
        new_path: "",
        name: "",
        header: [""],
        body: [{
                index: 0,
                key: "",
            }],
    };

    function onAdd() {
        console.log(filePath);
        filePaths.push(filePath);
        filePaths = filePaths;
        filePath = {
            new_path: "",
            name: "",
            header: [""],
            body: [{
                index: 0,
                key: "",
            }],
        };
        filePath = filePath;
    }

    function onSubmit() {
        let response = fetch("/api/file_stitched_paths", {
            method: "PUT",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(filePaths)
        }).then(response => {
            response.json().then((data) => {
                filePaths = filePaths.filter((Entry, index) => JSON.parse(data)[index] !== "OK")
            });
        });
    }
</script>

<div style="margin-left: 10px;">
    <h1 style="color: #eceff4;">File Stitch Paths</h1>
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

<div style="margin-left: 10px;">
    
</div>
