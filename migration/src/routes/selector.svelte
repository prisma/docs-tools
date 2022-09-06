<script lang="ts">
    import { page } from '$app/stores';

    interface item {
        name: string;
        link: string;
    }
    export let items: item[];
</script>

<div class="outer">
    {#each items as item}
        {#if item.link === $page.url.pathname}
            <div class="inner" style="background-color: #2e3440;">
                <a href={item.link} class="link">{item.name}</a>
            </div>
        {:else}
            <div class="inner">
                <a href={item.link} class="link">{item.name}</a>
            </div>
        {/if}
    {/each}
</div>

<style lang="scss">
    .inner {
        width: 80px;
        height: 100%;
        text-align: center;
        text-decoration: none;
    }
    .outer {
        display: flex;
        flex-direction: row;
        height: 20px;
        width: 100%;
        background-color: #3b4252;
    }
    .link {
        text-decoration: none;
        color: #d8dee9;
        font-family: "Roboto", sans-serif;
        font-size: 12px;
    }
</style>