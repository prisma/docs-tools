<script lang="ts">
    import type {FilePath} from "./common";
    import "../../app.scss";
    import "../entry.scss";
    
    export let type: string = "";
    export let entry: FilePath
</script>

<div class="w-72">
    <input bind:value={entry.name} placeholder="Name" class={"relative w-full h-9 field top " + type}>
    <input bind:value={entry.current_path} placeholder="Current Path" class={"relative w-full h-9 field middle " + type}>
    <input bind:value={entry.new_path} placeholder="New Path" class={"relative w-full h-9 field middle " + type}>
    <input bind:value={entry.redirect} placeholder="Redirect" class={"relative w-full h-9 field bottom " + type}>
</div>

<style lang="scss">
    
</style>
