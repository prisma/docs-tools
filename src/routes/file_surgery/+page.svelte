<script lang="ts">
    import "../pages.scss";
    import Entries from "../entries.svelte";

    interface FileSurgeryPath {
        [key: string]: string | undefined;
        current: string;
        new: string;
        redirect?: string;
        name?: string;
    }

    interface FileSurgeyPaths {
        data: FileSurgeryPath[];
    }

    let fileSurgeryPath: FileSurgeryPath = {
        current: "",
        new: "",
        redirect: "",
        name: ""
    };

    let fileSurgeryPaths: FileSurgeyPaths = {
        data: []
    };

    function onAdd() {
        if (fileSurgeryPath.name === "") {
            delete fileSurgeryPath.name;
        }
        if (fileSurgeryPath.redirect === "") {
            delete fileSurgeryPath.redirect;
        }
        fileSurgeryPaths.data.push(fileSurgeryPath);
        fileSurgeryPaths = fileSurgeryPaths;
        fileSurgeryPath = {
            current: "",
            new: "",
            redirect: "",
            name: ""
        };
    }

    function onSubmit() {
        let response = fetch("/api/create_file_surgery_paths", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(fileSurgeryPaths)
        });
        fileSurgeryPaths.data = [];
    }
</script>

<div style="margin-left: 10px;">
    <h1 style="color: #eceff4;">File Move Paths</h1>
    <form on:submit|preventDefault={onAdd}>
        <label>name*</label>
        <input type="text" class="inner-each top selected" bind:value={fileSurgeryPath.name}>
        <label>current</label>
        <input type="text" class="inner-each middle selected" bind:value={fileSurgeryPath.current}>
        <label>new</label>
        <input type="text" class="inner-each middle selected" bind:value={fileSurgeryPath.new}>
        <label>redirect*</label>
        <input type="text" class="inner-each middle selected" bind:value={fileSurgeryPath.redirect}>
        <div style="display: flex; flex-direction: row; margin-left: 100px; width: 200px">
            <button type="button" class="button left selected" on:click={onAdd}>Add</button>
            <button type="button" class="button right selected" on:click={onSubmit}>Submit</button>
        </div>
    </form>

</div>

<div style="margin-left: 10px;">
    <Entries entries={fileSurgeryPaths} items={["name", "current", "new", "redirect"]}/>
</div>