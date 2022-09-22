<script lang="ts">
    import type {BodyPart, FilePath} from "./common";
    import "../pages.scss";
    import Entry from "./entry.svelte"

    let filePaths: FilePath[] = [];

    let filePath: FilePath = {
        new_path: "",
        name: "",
        header: [
            ["title", ""],
            ["metaTitle", ""],
            ["metaDescription", ""]
        ],
        body: [{
                index: 0,
                key: "",
            }],
    };

    function onAdd() {
        filePaths.push(filePath);
        filePaths = filePaths;
        filePath = {
            new_path: "",
            name: "",
            header: [
                ["title", ""],
                ["metaTitle", ""],
                ["metaDescription", ""]
            ],
            body: [{
                index: 0,
                key: "",
            }],
        };
        filePath = filePath;
    }

    function onSubmit() {
        let requestcontents = [];
        for (let i = 0; i < filePaths.length; i++) {
            interface header {
                [key: string]: any;
            }
            let header : header = {};
            let body: BodyPart[] = [];
            for (let j = 0; j < filePaths[i].header.length; j++) {
                header[filePaths[i].header[j][0]] = filePaths[i].header[j][1];
            }
            for (let j = 0; j < filePaths[i].body.length; j++) {
                if (filePaths[i].body[j].key !== "") {
                    body.push(filePaths[i].body[j]);
                }
            }
            requestcontents.push({
                name: filePaths[i].name,
                new_path: filePaths[i].new_path,
                header: header,
                body: body,
            });
        }
        console.log(requestcontents);
        let response = fetch("/api/file_stitched_paths", {
            method: "PUT",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(requestcontents),
        }).then(response => {
            response.json().then((data) => {
                filePaths = filePaths.filter((Entry, index) => data[index] !== "OK")
            });
        });
    }
</script>

<div style="margin-left: 10px;">
    <h1 style="color: #eceff4;">File Stitch Paths</h1>
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

<div style="margin-left: 10px;">
    
</div>
