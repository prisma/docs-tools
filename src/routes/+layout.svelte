<script lang="ts">
    import Selector from "./selector.svelte";
</script>

<Selector items={[{name: "file_move", link: "/file_move"}, {name: "file_delete", link: "/file_delete"}]}/>
<slot></slot>

<style lang="scss">
    :global(body) {
        padding: 0%;
        margin: 0%;
    }
</style>