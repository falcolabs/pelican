<script lang="ts">
    import Footer from "../../components/Footer.svelte";
    import NavBar from "../../components/NavBar.svelte";
    import ScoreBoard from "../../components/ScoreBoard.svelte";

    const COLOR = "#DA215B";
    const CODENAME = "anh";
    const DISPLAY_NAME = "Chuyên Anh";
    const SLOGAN = "#pinkstorm";
</script>

<svelte:head>
    <title>Lưu ý & điều khoản sử dụng</title>
</svelte:head>

<div class="container px-7 md:px-36 md:pt-12">
    <p>Được cập nhật lần cuối vào ngày 16 tháng 6 năm 2025.</p>
    <h1>Điều khoản sử dụng</h1>
    <h2>Chào mừng bạn đến với Dự án Pelican!</h2>
    <p>
        Bằng việc sử dụng thông tin từ Dự án Pelican ("Dự Án"), bạn đồng ý với những điều khoản sau.
        Nếu bạn không đồng ý, không hiểu, hay không đồng ý một phần với những điều này, bạn không
        được sử dụng thông tin của Dự Án.
    </p>
    <p>
        Nếu bạn cần đọc thông báo miễn trừ trách nhiệm, bấm vào <a href="#mientru"
            ><strong>đây</strong></a
        >.
    </p>
    <h2>Về dự án</h2>
    <p>
        Cảm ơn bạn đã truy cập vào trang thông tin của Dự Án. Chúng tôi cung cấp cho người dùng
        những thông tin cần thiết, có thể bình duyệt (xem <a
            href="https://github.com/falcolabs/pelican">mã nguồn của dự án</a
        >).
    </p>
    <h2>Cập nhật điều khoản này</h2>
    <p>
        Dự án có quyền cập nhật những điều khoản này mà không báo trước. Nội dung điều khoản mới sẽ
        được thông báo trên trang chủ của Dự án.
    </p>
    <h2 id="hanhvibicam">Hành vi bị cấm</h2>
    <p>
        Bạn không được phép sử dụng Thông tin được Dự án cung cấp để thực hiện những hành vi sau đây
        (xem <a href="#dinhchi"><strong>Đình chỉ và Chấm dứt</strong></a>):
    </p>
    <div>
        <li>sử dụng Thông tin mà Dự án cung cấp để vi phạm pháp luật,</li>
        <li>
            sử dụng Thông tin mà Dự án cung cấp để gây hoang mang trong dư luận, lan truyền thông
            tin sai lệch,
        </li>
        <li>giả mạo Dự án,</li>
        <li>xúc phạm đến phẩm giá, danh dự của người khác, thí sinh khác,</li>
        <li>vi phạm luật bản quyền,</li>
        <li>
            xâm nhập, "hack", hay truy cập trái phép vào các trang thông tin và dữ liệu của Dự án
            khi chưa được cho phép,
        </li>
        <li>sử dụng thông tin của Dự án để lừa đảo người khác, thí sinh khác,</li>
        <li>
            thực hiện bất kỳ hành vi gì làm đình trệ trang của Dự án, không cho người khác truy cập
            vào trang của Dự án, DDoS (tấn công từ chối dịch vụ) trang của Dự án.
        </li>
    </div>

    <h2 id="dinhchi">Đình chỉ và Chấm dứt</h2>
    <p>
        Nếu bạn vi phạm những hành vi bị cấm này, việc sử dụng thông tin Dự án của bạn sẽ bị đình
        chỉ vĩnh viễn.
    </p>

    <h2>Khiếu nại pháp lý</h2>
    <p>
        Nếu bạn muốn Dự án gỡ phần thông tin nào vì lý do pháp lý, liên hệ <a
            href="mailto:support@falcolabs.org">support@falcolabs.org</a
        >. Chúng tôi sẽ giải quyết sớm nhất có thể.
    </p>
    <h2 id="riengtu">Quyền riêng tư của bạn</h2>
    <p>
        Chúng tôi không thu thập bất kỳ thông tin cá nhân nào của bạn (xem <a
            href="https://github.com/falcolabs/pelican">mã nguồn của dự án</a
        >).
    </p>
    <h2 id="mientru">Tuyên bố miễn trừ trách nhiệm</h2>
    <p class="caps">
        Thông tin này chỉ được dự án cung cấp khi có thể. Dự án hoàn toàn không bảo đảm hay hợp đồng
        với người dùng về điểm thi và kết quả của thí sinh. Người dùng tự chịu trách nhiệm về việc
        sử dụng thông tin Dự án của mình.
    </p>
    <p class="caps">
        Dự án hoàn toàn không chịu bất kỳ trách nhiệm pháp lý nào gây ra bởi người dùng sử dụng
        thông tin Dự án sai điều khoản này hoặc vi phạm pháp luật.
    </p>
    <p class="caps">
        Thông tin của dự án không phải lúc nào cũng cập nhật trực tiếp và chính xác đến từng giây.
        Dự án sẽ cập nhật thông tin khi có thể.
    </p>
    <p class="caps">
        Dự án hoàn toàn không nhằm mục đích gây ra hoang mang dư luận hay lan truyền thông tin sai
        lệch (xem <a href="https://github.com/falcolabs/pelican">Bình duyệt</a>). Dự án không nhận
        ủng hộ hay tài trợ từ bất kỳ tổ chức nào (kể cả FalcoLabs Research)
    </p>
    <p>
        This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
        without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
        See the GNU Affero General Public License for more details.
    </p>
    <br /><br /><br />
    <p>Được cập nhật lần cuối vào ngày 16 tháng 6 năm 2025.</p>
    <br /><br /><br />
</div>

<style>
    .container {
        margin-top: 3rem !important;
        margin-left: 10%;
        margin-right: 10%;
        max-width: 80vw;
    }
    li {
        margin-left: 1rem;
        font-weight: 500;
    }

    h1 {
        font-size: 3rem;
        font-weight: bold;
        margin-top: 1rem !important;
    }

    a {
        color: #1e93e6;
    }

    .caps {
        text-transform: uppercase !important;
    }

    h2 {
        font-size: 2rem;
        font-weight: bold;
        margin-top: 1rem !important;
    }

    p {
        font-weight: 500;
        font-size: 1rem;
        margin-bottom: 0.5rem !important;
    }

    @media (width <= 48rem /* 768px */) {
        h1 {
            font-size: 2rem;
        }

        .container {
            margin-top: 3rem !important;
            margin-left: 0;
            margin-right: 0;
        }

        h2 {
            font-size: 1.5rem;
        }

        .container {
            max-width: 100vw;
        }
    }
</style>
