<script lang="ts">
    import ScoreBoard from "@/components/ScoreBoard.svelte";

    const COLOR = "#6D7075";
    const CODENAME = "dia";
    const DISPLAY_NAME = "Chuyên Địa";
    const SLOGAN = "#diachat";
</script>

<div class="px-7 pt-6 md:px-36 md:pt-12">
    <ScoreBoard color={COLOR} codename={CODENAME} displayname={DISPLAY_NAME} slogan={SLOGAN} />
</div>
