<script lang="ts">
    import type { Snippet } from "svelte";

    const { href, children }: { href: string; children: Snippet } = $props();
</script>

<a {href} role="button" class="neobrutal card flex flex-row items-start gap-4 border py-7">
    {@render children()}
</a>

<style>
    .neobrutal {
        border-radius: 18px;
        border: 1px solid #000;
        background: #fff;
        box-shadow: 4px 4px 0px 0px #000;
        transition: ease 100ms;
    }

    .neobrutal:hover {
        background: #f4f4f4;
        box-shadow: none;
        transform: translateX(4px) translateY(4px);
    }

    .card {
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: row;
        width: 25rem;
    }

    @media (width <= 48rem /* 768px */) {
        .card {
            display: flex;
            align-items: center;
            justify-content: center;
            flex-direction: row;
            width: 80vw;
        }
    }
</style>
