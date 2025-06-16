<script lang="ts">
    let { until, children } = $props();
</script>

<div>
    {#if until}
        {@render children()}
    {:else}
        Đang tải...
    {/if}
</div>
