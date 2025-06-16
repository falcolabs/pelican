<div class="container">
    <div class="flex h-12 flex-row items-center justify-center gap-3 lg:justify-start">
        <img src="/logo.svg" alt="logo Dự án Pelican" />
        <img class="hide h-7 lg:block" src="/falcologo.svg" alt="logo FalcoLabs Research" />
    </div>
    <br />
    <div class="hidden lg:block">
        <br /><br />
        <div class="align-center hidden items-center justify-center gap-7 font-semibold md:flex">
            <a class="hover:underline" href="/">điểm chuyên</a>
            <a class="hover:underline" href="https://github.com/falcolabs/pelican"
                >cách chúng tôi thu thập số liệu</a
            >
            <a class="hover:underline" href="/disclaimer">lưu ý & điều khoản</a>
            <a class="hover:underline" href="https://github.com/falcolabs/pelican">mã nguồn</a>
        </div>
        <br />
    </div>
    <div class="block">
        <div class="align-center flex items-center justify-center gap-3 font-semibold">
            <a
                class="hover:underline"
                aria-label="GitHub"
                href="https://github.com/falcolabs/pelican"><i class="fa-brands fa-github fa-xl"></i></a
            >
            <a
                class="hover:underline"
                aria-label="Facebook"
                href="https://www.facebook.com/project.pelican.cbn/"
                ><i class="fa-brands fa-facebook fa-xl"></i></a
            >
        </div>
        <br />
    </div>
    <div class="flex w-full items-center justify-center">
        <p class="max-w-[70vw] text-center text-sm text-gray-500">
            Bản quyền &copy; 2025 Dự án Pelican. Trang này và thông tin trên trang được phân phối
            theo giấy phép AGPL-3.0
        </p>
    </div>
</div>

<style>
    .hide {
        display: none !important;
    }

    .container {
        background-color: #fceee3;
        display: flex;
        flex-direction: column;
        border-top: 1px solid black;
        padding-top: 1.5rem;
        padding-left: 1rem;
        padding-right: 1rem;
        padding-bottom: 0.5rem;
        width: 100% !important;
        max-width: 100vw !important;
    }

    @media (width >= 64rem /* 1024px */) {
        .hide {
            display: block !important;
        }

        .container {
            display: flex;
            padding-top: 3rem;
            padding-left: 10rem;
            padding-right: 10rem;
            padding-bottom: 0.5rem;
        }
    }
</style>
