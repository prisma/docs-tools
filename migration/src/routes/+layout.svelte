<script lang="ts">
    import Selector from "./selector.svelte";
    import {database, setDatabase} from "../global";
    import "./entry.scss";
    let _database = database;
</script>

<Selector items={[{name: "File Move", link: "/file_move"}, {name: "File Delete", link: "/file_delete"}, {name: "File Surgery", link: "/file_surgery"}, {name: "File Stitch", link: "/file_stitch"}]}/>
<input bind:value={_database} on:input={() => {setDatabase(_database)}} placeholder="Database* (Leave blank for default)" class={"relative w-full h-9 field button"} style={"width: 300px; margin: 8px; margin-left: 18px"}/>
<slot></slot>

<style lang="scss">
    :global(body) {
        padding: 0%;
        margin: 0%;
        background-color: #4c566a;
        color: #d8dee9;
        font-family: "Roboto", sans-serif;
    }
</style>
