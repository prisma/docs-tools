<script lang="ts">
    import type {BodyPart, FilePath} from "./common";
    import "../../app.scss";
    import "../entry.scss";
    
    export let type: string = "";
    export let entry: FilePath
    if (JSON.stringify(entry.headers) == "[]") {
        entry.headers.push("")
        entry = entry
    }
    
    function onaddheader() {
        entry.headers.push("")
        entry = entry
    }

    function onaddbody() {
        entry.body.push({
            index: 0,
            key: "",
        })
        entry = entry
    }
</script>

<div class="w-72">
    <input bind:value={entry.name} placeholder="Name" class={"relative w-full h-9 field top " + type}>
    <input bind:value={entry.new_path} placeholder="Path" class={"relative w-full h-9 field bottom " + type}>
    {#each entry.headers as _, index}
        <div class="relative w-full flex">
            {#if index === 0}
                <button type="button" class="flex-none w-9 h-9" on:click={onaddheader}>+</button>
            {:else}
                <div class="flex-none w-9 h-9"></div>
            {/if}
            <input bind:value={entry.headers[index]} placeholder="Header" class={"flex-auto h-9 field single " + type}>
            <button type="button" class="flex-none w-9 h-9" on:click={()=>{entry.headers.splice(index, 1);  if (entry.headers.length <= 0) {entry.headers = [""]}; entry = entry }}>-</button>
        </div>
    {/each}
    {#each entry.body as _, index}
        <div class="relative w-full flex">
            {#if index === 0}
                <button type="button" class="flex-none w-9 h-9" on:click={onaddbody}>+</button>
            {:else}
                <div class="flex-none w-9 h-9"></div>
            {/if}
            <input type="number" bind:value={entry.body[index].index} placeholder="Index" class={"flex-auto h-9 field single " + type}>
            <button type="button" class="flex-none w-9 h-9" on:click={()=>{entry.body.splice(index, 1); if (entry.body.length <= 0) {entry.body = [{index: 0, key: ""}]}; entry = entry}}>-</button>
        </div>
        <div class="relative w-full flex">
            <div class="flex-none w-9 h-9"></div>
            <input bind:value={entry.body[index].key} placeholder="Key" class={"flex-auto h-9 field single " + type}>
            <div class="flex-none w-9 h-9"></div>
        </div>
    {/each}
</div>

<style lang="scss">
    
</style>
