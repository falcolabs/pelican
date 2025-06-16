<script lang="ts">
    let { color, displayname, slogan, stats } = $props();
</script>

<div class="flex flex-col gap-4 lg:flex-row lg:justify-between lg:gap-12">
    <div class="flex min-w-fit flex-row items-start gap-4">
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
                <path d="M19.9074 10.1927L37.0776 0.337173V20.0482L19.9074 10.1927Z" fill={color} />
                <path d="M36.8287 21.0781L18.912 11.2226V30.9337L36.8287 21.0781Z" fill={color} />
                <path d="M24.8842 32.9531L42.0544 23.0976V42.8087L24.8842 32.9531Z" fill={color} />
                <path d="M24.8842 54.7239L42.0544 44.8684V64.5795L24.8842 54.7239Z" fill={color} />
                <path d="M36.8287 43.3438L18.912 33.0596V53.6279L36.8287 43.3438Z" fill={color} />
            </g>
            <defs>
                <clipPath id="clip0_4_444">
                    <rect width="43" height="76" fill="white" />
                </clipPath>
            </defs>
        </svg>
        <div class="text-4xl leading-9">
            Khối
            <br />
            <span class="font-bold" style={"color:" + color + ";"}>{displayname}</span>
            <p class="text-lg font-semibold" style={"color:" + color + ";"}>
                {slogan}
            </p>
        </div>
    </div>

    <div class="md:gap-15 flex flex-row flex-wrap gap-8" style="row-gap: 1rem;">
        <div>
            <p class="text-lg font-semibold">SỐ THÍ SINH</p>
            <p class="font-[Montserrat] text-5xl font-semibold">{stats.candidates}</p>
        </div>
        <div>
            <p class="text-lg font-semibold">ĐIỂM ĐỖ DỰ ĐOÁN</p>
            <p class="font-[Montserrat] text-5xl font-semibold">{stats.prediction.toFixed(2)}</p>
        </div>
        <div>
            <p class="text-lg font-semibold">TỈ LỆ ĐỖ</p>
            <p class="font-[Montserrat] text-5xl font-semibold">{(stats.rate * 100).toFixed(2)}%</p>
        </div>
    </div>
</div>
