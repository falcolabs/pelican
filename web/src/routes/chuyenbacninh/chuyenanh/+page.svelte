<script lang="ts">
    import ScoreBoard from "@/components/ScoreBoard2.svelte";

    const COLOR = "#DA215B";
    const CODENAME = "anh";
    const DISPLAY_NAME = "Chuyên Anh";
    const SLOGAN = "#pinkstorm";
</script>

<div class="px-7 pt-6 md:px-36 md:pt-12">
    <ScoreBoard color={COLOR} codename={CODENAME} displayname={DISPLAY_NAME} slogan={SLOGAN} />
</div>
