<script lang="ts">
    import "../pages.scss";
    import Entry from "./stitch_entry.svelte"
   
    interface BodyPart {
        index: number;
        key: string;
    }
    interface FileStitchPath { 
        new_path: string;
        name?: string;
        headers: string[]; 
        body: BodyPart[];
    };

    let fileStitchPaths: FileStitchPath[] = [];

    let fileStitchPath: FileStitchPath = {
        new_path: "",
        name: "",
        headers: [],
        body: [],
    };

    function onAdd() {
        if (fileStitchPath.name === "") { delete fileStitchPath.name; }
        fileStitchPaths.push(fileStitchPath);
        fileStitchPaths = fileStitchPaths;
        fileStitchPath = {
            new_path: "",
            name: "",
            headers: [],
            body: [],
        };
    }

    function onSubmit() {
        let response = fetch("/api/file_stitched_paths", {
            method: "PUT",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(fileStitchPaths)
        });
        fileStitchPaths = [];
    }
</script>

<div style="margin-left: 10px;">
    <h1 style="color: #eceff4;">File Move Paths</h1>
    <Entry entry={fileStitchPath} type="selected"/>
    <div class="flex w-72">
        <button class="w-full button left selected" onclick={onAdd}>
            Add
        </button>
        <button class="w-full button right selected" onclick={onSubmit}>
            Submit
        </button>
    </div>
    {#each fileStitchPaths as entry}
        <Entry entry={entry} type=""/>
    {/each}
</div>

<div style="margin-left: 10px;">
    
</div>
