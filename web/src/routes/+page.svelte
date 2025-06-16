<script lang="ts">
    import Disclaimer from "../components/Disclaimer.svelte";
    import Footer from "../components/Footer.svelte";
    import NavBar from "../components/NavBar.svelte";
</script>

<NavBar />
<div class="px-7 pt-6 md:px-36 md:pt-12">
    <h1 class="text-center text-2xl font-bold">
        Bấm vào ô của các khối chuyên để xem thông tin chi tiết và bảng điểm
    </h1>
    <Disclaimer />
    <br />
    <div class="flex flex-col flex-wrap items-center justify-center gap-4 lg:flex-row">
        {#each [{ classes: 2, color: ["#EBEC94", "#A700FE"], displayname: "Chuyên Văn", codename: "van" }, { classes: 1, color: "#FE0000", displayname: "Chuyên Tin", codename: "tin" }, { classes: 1, color: "#3F5FFF", displayname: "Chuyên Lý", codename: "ly" }, { classes: 1, color: "#33B7C2", displayname: "Chuyên Hóa", codename: "hoa" }, { classes: 2, color: ["#109E14", "#109E14"], displayname: "Chuyên Toán", codename: "toan" }, { classes: 1, color: "#754119", displayname: "Chuyên Sử", codename: "su" }, { classes: 1, color: "#6D7075", displayname: "Chuyên Địa", codename: "dia" }, { classes: 1, color: "#FE6603", displayname: "Chuyên Sinh", codename: "sinh" }, { classes: 1, color: "#DA215B", displayname: "Chuyên Anh", codename: "anh" }, { classes: 1, color: "#010101", displayname: "Chuyên Trung", codename: "trung" }, { classes: 1, color: "#010101", displayname: "Chuyên Hàn", codename: "han" }] as { classes, color, displayname, codename }}
            {#if classes === 1}
                <a
                    href={`/chuyen${codename}`}
                    role="button"
                    class="neobrutal card flex flex-row items-start gap-4 border py-7"
                >
                    <svg
                        xmlns="http://www.w3.org/2000/svg"
                        width="43"
                        height="76"
                        viewBox="0 0 43 76"
                        fill="none"
                    >
                        <g clip-path="url(#clip0_4_444)">
                            <path
                                d="M0 65.45L18.5292 55.2188L36.8287 65.5456L18.4963 76L0 65.45Z"
                                fill={color}
                            />
                            <path
                                d="M17.9167 11.6771L0 21.8272L0.0649154 64.125L17.9167 53.7506V11.6771Z"
                                fill={color}
                            />
                            <path
                                d="M19.9074 10.1927L37.0776 0.337173V20.0482L19.9074 10.1927Z"
                                fill={color}
                            />
                            <path
                                d="M36.8287 21.0781L18.912 11.2226V30.9337L36.8287 21.0781Z"
                                fill={color}
                            />
                            <path
                                d="M24.8842 32.9531L42.0544 23.0976V42.8087L24.8842 32.9531Z"
                                fill={color}
                            />
                            <path
                                d="M24.8842 54.7239L42.0544 44.8684V64.5795L24.8842 54.7239Z"
                                fill={color}
                            />
                            <path
                                d="M36.8287 43.3438L18.912 33.0596V53.6279L36.8287 43.3438Z"
                                fill={color}
                            />
                        </g>
                        <defs>
                            <clipPath id="clip0_4_444">
                                <rect width="43" height="76" fill="white" />
                            </clipPath>
                        </defs>
                    </svg>
                    <div class="text-2xl leading-7 md:text-4xl md:leading-9">
                        Khối
                        <br />
                        <span class="font-bold" style={"color:" + color + ";"}>{displayname}</span>
                    </div>
                </a>
            {:else}
                <a
                    href={`/chuyen${codename}`}
                    role="button"
                    class="neobrutal card flex flex-row items-start gap-4 border py-7"
                >
                    <svg
                        xmlns="http://www.w3.org/2000/svg"
                        width="43"
                        height="76"
                        viewBox="0 0 43 76"
                        fill="none"
                    >
                        <g clip-path="url(#clip0_4_444)">
                            <path
                                d="M0 65.45L18.5292 55.2188L36.8287 65.5456L18.4963 76L0 65.45Z"
                                fill={color[0]}
                            />
                            <path
                                d="M17.9167 11.6771L0 21.8272L0.0649154 64.125L17.9167 53.7506V11.6771Z"
                                fill={color[0]}
                            />
                            <path
                                d="M19.9074 10.1927L37.0776 0.337173V20.0482L19.9074 10.1927Z"
                                fill={color[0]}
                            />
                            <path
                                d="M36.8287 21.0781L18.912 11.2226V30.9337L36.8287 21.0781Z"
                                fill={color[0]}
                            />
                            <path
                                d="M24.8842 32.9531L42.0544 23.0976V42.8087L24.8842 32.9531Z"
                                fill={color[0]}
                            />
                            <path
                                d="M24.8842 54.7239L42.0544 44.8684V64.5795L24.8842 54.7239Z"
                                fill={color[0]}
                            />
                            <path
                                d="M36.8287 43.3438L18.912 33.0596V53.6279L36.8287 43.3438Z"
                                fill={color[0]}
                            />
                        </g>
                        <defs>
                            <clipPath id="clip0_4_444">
                                <rect width="43" height="76" fill="white" />
                            </clipPath>
                        </defs>
                    </svg>
                    <svg
                        xmlns="http://www.w3.org/2000/svg"
                        width="43"
                        height="76"
                        viewBox="0 0 43 76"
                        fill="none"
                    >
                        <g clip-path="url(#clip0_4_444)">
                            <path
                                d="M0 65.45L18.5292 55.2188L36.8287 65.5456L18.4963 76L0 65.45Z"
                                fill={color[1]}
                            />
                            <path
                                d="M17.9167 11.6771L0 21.8272L0.0649154 64.125L17.9167 53.7506V11.6771Z"
                                fill={color[1]}
                            />
                            <path
                                d="M19.9074 10.1927L37.0776 0.337173V20.0482L19.9074 10.1927Z"
                                fill={color[1]}
                            />
                            <path
                                d="M36.8287 21.0781L18.912 11.2226V30.9337L36.8287 21.0781Z"
                                fill={color[1]}
                            />
                            <path
                                d="M24.8842 32.9531L42.0544 23.0976V42.8087L24.8842 32.9531Z"
                                fill={color[1]}
                            />
                            <path
                                d="M24.8842 54.7239L42.0544 44.8684V64.5795L24.8842 54.7239Z"
                                fill={color[1]}
                            />
                            <path
                                d="M36.8287 43.3438L18.912 33.0596V53.6279L36.8287 43.3438Z"
                                fill={color[1]}
                            />
                        </g>
                        <defs>
                            <clipPath id="clip0_4_444">
                                <rect width="43" height="76" fill="white" />
                            </clipPath>
                        </defs>
                    </svg>
                    <div class="text-2xl leading-7 md:text-4xl md:leading-9">
                        Khối
                        <br />
                        <span class="font-bold" style={"color:" + color + ";"}>{displayname}</span>
                    </div>
                </a>
            {/if}
        {/each}
    </div>
</div>
<br /><br /><br />
<Footer />

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
