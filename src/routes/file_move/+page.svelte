<script lang="ts">
    import "../pages.scss";
    import Entries from "../entries.svelte";

    interface FileMovePath {
        [key: string]: string | undefined;
        current: string;
        new: string;
        name?: string;
    }

    interface FileMovePaths {
        data: FileMovePath[];
    }

    let fileMovePath: FileMovePath = {
        current: "",
        new: "",
        name: ""
    };

    let fileMovePaths: FileMovePaths = {
        data: []
    };

    function onAdd() {
        if (fileMovePath.name === "") {
            delete fileMovePath.name;
        }
        fileMovePaths.data.push(fileMovePath);
        fileMovePaths = fileMovePaths;
        fileMovePath = {
            current: "",
            new: "",
            name: ""
        };
    }

    function onSubmit() {
        let response = fetch("/api/file_move_paths", {
            method: "PUT",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(fileMovePaths)
        });
        fileMovePaths.data = [];
    }
</script>

<div style="margin-left: 10px;">
    <h1 style="color: #eceff4;">File Move Paths</h1>
    <form on:submit|preventDefault={onAdd}>
        <label>name*</label>
        <input type="text" class="inner-each top selected" bind:value={fileMovePath.name}>
        <label>current</label>
        <input type="text" class="inner-each middle selected" bind:value={fileMovePath.current}>
        <label>new</label>
        <input type="text" class="inner-each middle selected" bind:value={fileMovePath.new}>
        <div style="display: flex; flex-direction: row; margin-left: 100px; width: 200px">
            <button type="button" class="button left selected" on:click={onAdd}>Add</button>
            <button type="button" class="button right selected" on:click={onSubmit}>Submit</button>
        </div>
    </form>

</div>

<div style="margin-left: 10px;">
    <Entries entries={fileMovePaths} items={["name", "current", "new"]}/>
</div>