<script lang="ts">
    import ScoreBoard from "@/components/ScoreBoard.svelte";

    const COLOR = "#754119";
    const CODENAME = "su";
    const DISPLAY_NAME = "Chuyên Sử";
    const SLOGAN = "#satthat";
</script>

<div class="px-7 pt-6 md:px-36 md:pt-12">
    <ScoreBoard color={COLOR} codename={CODENAME} displayname={DISPLAY_NAME} slogan={SLOGAN} />
</div>
