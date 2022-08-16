<script lang="ts">
    interface fileDeletePath {
        path: string;
        redirect?: string;
        name?: string;
    }

    interface fileDeletePaths {
        data: fileDeletePath[];
    }

    let fileDeletePath: fileDeletePath = {
        path: "",
        redirect: "",
        name: ""
    };

    let fileDeletePaths: fileDeletePaths = {
        data: []
    };

    function onAdd() {
        if (fileDeletePath.name === "") {
            delete fileDeletePath.name;
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
        let response = fetch("/api/create_file_move_paths", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(fileDeletePaths)
        });
        fileDeletePaths.data = [];
    }
</script>

<div style="margin-left: 10px;">
    <h1>File Delete Paths</h1>
    <form on:submit|preventDefault={onAdd}>
        <label>name*</label>
        <input type="text" bind:value={fileDeletePath.name}>
        <label>path</label>
        <input type="text" bind:value={fileDeletePath.path}>
        <label>redirect*</label>
        <input type="text" bind:value={fileDeletePath.redirect}>
        <button type="submit">Add</button>
    </form>

    <button on:click={onSubmit}>Submit</button>
</div>

<div style="margin-left: 10px;">
    {#each fileDeletePaths.data as entry, index}
        <div class="outer-each">
            <div class="inner-each top">{entry.name || ""}</div>
            <div class="inner-each middle">{entry.path}</div>
            <div class="inner-each bottom">{entry.redirect || ""}</div>
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