<script lang="ts">
    import Selector from "./selector.svelte";
</script>

<Selector items={[{name: "File Move", link: "/file_move"}, {name: "File Surgery", link: "/file_surgery"}, {name: "File Delete", link: "/file_delete"}]}/>
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
