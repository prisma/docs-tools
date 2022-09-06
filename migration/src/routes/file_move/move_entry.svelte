<script lang="ts">
    import "../../app.scss";
    import "../entry.scss";
    import Plus from "../plus.svg"
    import Delete from "../delete.svg"
    
    interface BodyPart {
        index: number;
        key: string;
    }
    interface FileStitchPath { 
        new_path: string;
        name?: string;
        headers: string[];
        body: BodyPart[];
    };
    export let type: string = "";
    export let entry: FileStitchPath
    if (JSON.stringify(entry.headers) == "[]") {
        entry.headers.push("")
        entry = entry
    }
    let plusicon = { icon: Plus, props: { width: '10px', height: '10px' }}
    let deleteicon = { icon: Delete, props: { width: '10px', height: '10px'}}
    function onaddheader() {
        entry.headers.push("")
        entry = entry
    }
</script>

<div class="w-72">
    <input value={entry.name} placeholder="Name" class={"relative w-full h-9 field top " + type}>
    <input value={entry.new_path} placeholder="Path" class={"relative w-full h-9 field bottom " + type}>
    {#each entry.headers as _, index}
        {#if index === 0}
            <div class="relative w-full flex">
                <button class="flex-none w-9 h-9" onclick={onaddheader}>+</button>
                <input value={entry.headers[index]} placeholder="Header" class={"flex-auto h-9 field single " + type}>
                <icon data={deleteicon.icon}{deleteicon.props} class="flex-none"/>
            </div>
        {:else}
            <div class="relative w-full flex">
                <div class="flex-none w-9 h-9"></div>
                <input value={entry.headers[index]} placeholder="Header" class={"flex-auto h-9 field single " + type}>
                <icon data={deleteicon.icon}{deleteicon.props} class="flex-none"/>
            </div>
        {/if}
    {/each}
</div>

<style lang="scss">
    
</style>
