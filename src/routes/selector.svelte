<script lang="ts">
    interface item {
        name: string;
        link: string;

    }
    export let items: item[];
</script>

<div class="outer">
    {#each items as item}
        <a href={item.link} style="color: black;">{item.name}    </a>
    {/each}
</div>

<style lang="scss">
    .outer {
        display: flex;
        flex-direction: column;
        height: 20px;
        width: 100%;
        background-color: lightgrey;
    }
</style>