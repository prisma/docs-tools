<script lang="ts">
    export let entries: {
        data: {
            [key: string]: string | undefined;
        }[]
    };
    export let items: string[];
</script>

<div>
    {#each entries.data as entry, index}
        <div class="outer-each">
            {#each items as item, indexx}
                {#if indexx === 0}
                    <input value={entries.data[index][item] || null} class="inner-each top">
                {:else if indexx === items.length - 1}
                    <input value={entries.data[index][item] || null} class="inner-each bottom">
                {:else}
                    <input value={entries.data[index][item] || null} class="inner-each middle">
                {/if}
            {/each}
        </div>
    {/each}
</div>