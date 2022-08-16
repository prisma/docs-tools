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
        let response = fetch("/api/create_file_move_paths", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(fileMovePaths)
        });
        
    }
</script>

<div style="margin-left: 10px;">
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
</div>

<div style="margin-left: 10px;">
    {#each fileMovePaths.data as entry, index}
        <div class="outer-each">
            <div class="inner-each top">{entry.name}</div>
            <div class="inner-each middle">{entry.current}</div>
            <div class="inner-each bottom">{entry.new}</div>
        </div>
    {/each}
</div>

<style lang="scss">
    form {
        display: grid;
        grid-template-columns: 100px 200px;
    }

    .inner-each {
        display: flex;
        border: 1px solid gray;
        padding: 5px;
        &.top {
            border-top-left-radius: 5px;
            border-top-right-radius: 5px;
        }

        &.middle {
            border-top: 0px;
            border-bottom: 0px;
        }
        
        &.bottom {
            border-bottom-left-radius: 5px;
            border-bottom-right-radius: 5px;
        }
    }

    .outer-each {
        display: grid;
        width: 200px;
        //padding: 5px;
        margin: 10px;
        margin-left: 100px;
        //border: 1px solid gray;
        border-radius: 10px;
    }

    button {
        margin-left: 100px;
        width: 100px;
    }

</style>