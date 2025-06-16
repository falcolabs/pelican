<script lang="ts">
    let { data } = $props();
</script>

<div class="radius-[18px] tbl grid overflow-hidden border bg-white font-semibold">
    <span
        class="flex min-h-11 items-center justify-center px-4"
        style="grid-row: 1 / 1; grid-column: 1 / 1;">STT</span
    >
    <span
        class="flex min-h-11 items-center justify-center px-4"
        style="grid-row: 1 / 1; grid-column: 2 / 2;">SBD</span
    >
    <span class="flex min-h-11 items-center px-4" style="grid-row: 1 / 1; grid-column: 3 / 3;"
        >Tên thí sinh</span
    >
    <span class="flex min-h-11 items-center px-4" style="grid-row: 1 / 1; grid-column: 4 / 4;"
        >Trường</span
    >
    <span class="flex min-h-11 items-center px-4" style="grid-row: 1 / 1; grid-column: 5 / 5;"
        >Ngày sinh</span
    >
    <span class="flex min-h-11 items-center px-4" style="grid-row: 1 / 1; grid-column: 6 / 6;"
        >Tổng chuyên</span
    >
    <span class="flex min-h-11 items-center px-4" style="grid-row: 1 / 1; grid-column: 7 / 7;"
        >Tổng thường</span
    >
    <span class="flex min-h-11 items-center px-4" style="grid-row: 1 / 1; grid-column: 8 / 8;"
        >Toán</span
    >
    <span class="flex min-h-11 items-center px-4" style="grid-row: 1 / 1; grid-column: 9 / 9;"
        >Văn</span
    >
    <span class="flex min-h-11 items-center px-4" style="grid-row: 1 / 1; grid-column: 10 / 10;"
        >Anh</span
    >
    <span class="flex min-h-11 items-center px-4" style="grid-row: 1 / 1; grid-column: 11 / 11;"
        >Môn Chuyên</span
    >
    {#each data.result as row, i}
        <span
            class="flex min-h-11 items-center justify-center"
            style={`grid-row: ${i + 2} / span 1; grid-column: 1 / 1; ${i % 2 === 0 ? "background-color: #F0F0F0" : ""}`}
            >{i + 1}</span
        >
        <span
            class="flex min-h-11 items-center justify-center"
            style={`grid-row: ${i + 2} / span 1; grid-column: 2 / 2; ${i % 2 === 0 ? "background-color: #F0F0F0" : ""}`}
            >{row.sbd}</span
        >
        <span
            class="flex min-h-11 items-center"
            style={`grid-row: ${i + 2} / span 1; grid-column: 3 / 3; ${i % 2 === 0 ? "background-color: #F0F0F0" : ""}`}
            >{row.name}</span
        >
        <span
            class="flex min-h-11 items-center"
            style={`grid-row: ${i + 2} / span 1; grid-column: 4 / 4; ${i % 2 === 0 ? "background-color: #F0F0F0" : ""}`}
            >{row.school}</span
        >
        <span
            class="flex min-h-11 items-center justify-center"
            style={`grid-row: ${i + 2} / span 1; grid-column: 5 / 5; ${i % 2 === 0 ? "background-color: #F0F0F0" : ""}`}
            >{row.birthdate}</span
        >
        <span
            class="flex min-h-11 items-center justify-center"
            style={`grid-row: ${i + 2} / span 1; grid-column: 6 / 6; ${i % 2 === 0 ? "background-color: #F0F0F0" : ""}`}
            >{row.totalGifted}</span
        >
        <span
            class="flex min-h-11 items-center justify-center"
            style={`grid-row: ${i + 2} / span 1; grid-column: 7 / 7; ${i % 2 === 0 ? "background-color: #F0F0F0" : ""}`}
            >{row.totalNorm}</span
        >
        <span
            class="flex min-h-11 items-center justify-center"
            style={`grid-row: ${i + 2} / span 1; grid-column: 8 / 8; ${i % 2 === 0 ? "background-color: #F0F0F0" : ""}`}
            >{row.math}</span
        >
        <span
            class="flex min-h-11 items-center justify-center"
            style={`grid-row: ${i + 2} / span 1; grid-column: 9 / 9; ${i % 2 === 0 ? "background-color: #F0F0F0" : ""}`}
            >{row.lit}</span
        >
        <span
            class="flex min-h-11 items-center justify-center"
            style={`grid-row: ${i + 2} / span 1; grid-column: 10 / 10; ${i % 2 === 0 ? "background-color: #F0F0F0" : ""}`}
            >{row.eng}</span
        >
        <span
            class="flex min-h-11 items-center justify-center"
            style={`grid-row: ${i + 2} / span 1; grid-column: 11 / 11; ${i % 2 === 0 ? "background-color: #F0F0F0" : ""}`}
            >{row.gifted}</span
        >
    {/each}
</div>

<style>
    .tbl {
        overflow: scroll;
        grid-template-columns: 7% 20% 20% auto auto auto auto auto auto;
        border-radius: 18px;
        border: 1px solid #000;
        background: #fff;
        box-shadow: 4px 4px 0px 0px #000;
        margin-bottom: 1rem;
    }
</style>
