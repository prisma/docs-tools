<script lang="ts">
    import type {BodyPart, FilePath} from "./common";
    import "../../app.scss";
    import "../entry.scss";
    
    export let type: string = "";
    export let entry: FilePath
    if (JSON.stringify(entry.header) == "[]") {
        entry.header.push(["", ""])
        entry = entry
    }
    
    function onaddheader() {
        entry.header.push(["", ""])
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

<div class="w-96">
    <input bind:value={entry.name} placeholder="Name" class={"relative w-full h-9 field top " + type}>
    <input bind:value={entry.new_path} placeholder="Path" class={"relative w-full h-9 field bottom " + type}>
    {#each entry.header as _, index}
        <div class="relative w-full flex">
            {#if index === 0}
                <button type="button" class="flex-none w-9 h-9" on:click={onaddheader}>+</button>
            {:else}
                <div class="flex-none w-9 h-9"></div>
            {/if}
            <input bind:value={entry.header[index][0]} placeholder="Header" class={"flex-auto h-9 field single " + type}>
            <input bind:value={entry.header[index][1]} placeholder="" class={"flex-auto h-9 field single " + type}>
            <button type="button" class="flex-none w-9 h-9" on:click={()=>{entry.header.splice(index, 1);  if (entry.header.length <= 0) {entry.header = [["", ""]]}; entry = entry }}>-</button>
        </div>
    {/each}
    {#each entry.body as _, index}
        <div class="relative w-full flex">
            {#if index === 0}
                <button type="button" class="flex-none w-9 h-9" on:click={onaddbody}>+</button>
            {:else}
                <div class="flex-none w-9 h-9"></div>
            {/if}
            <input bind:value={entry.body[index].key} placeholder="Body" class={"flex-auto h-9 field single " + type}>
            <input type="number" bind:value={entry.body[index].index} class={"flex-none h-9 w-12 field single " + type}>
            <button type="button" class="flex-none w-9 h-9" on:click={()=>{entry.body.splice(index, 1); if (entry.body.length <= 0) {entry.body = [{index: 0, key: ""}]}; entry = entry}}>-</button>
        </div>
    {/each}
</div>

<style lang="scss">
    
</style>
