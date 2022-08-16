<script lang="ts">
    interface FileMovePath {
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
        if (fileMovePath.name = "") {
            delete fileMovePath.name;
        }
        fileMovePaths.data.push(fileMovePath);
        fileMovePath = {
            current: "",
            new: "",
            name: ""
        };
    }

    function onSubmit() {
        fetch("/api/file_move_paths", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(fileMovePaths)
        });
    }
</script>

<h1>File Move Paths</h1>
<form on:submit|preventDefault={onAdd}>
    <label>name*</label>
    <input type="text" bind:value={fileMovePath.name}>
    <label>current</label>
    <input type="text" bind:value={fileMovePath.current}>
    <label>new</label>
    <input type="text" bind:value={fileMovePath.new}>
    <button type="submit">Add</button>
</form>

<button on:click={onSubmit}>Submit</button>

{#each fileMovePaths.data as path}
    <div>
        <p>{path.name}</p>
        <p>{path.current}</p>
        <p>{path.new}</p>
    </div>
{/each}

<style lang="scss">

</style>