[![MIT License][license-shield]][license-url]



<br />
<p align="center">
  <a href="https://github.com/DaviesGit">
    <img src="readme_images/Ideal_Logo_Davies.ico" alt="Logo" width="150">
  </a>

  <h3 align="center">Maked by Davies</h3>

  <p align="center">
    Email: 1182176003@qq.com
<!--     <br />
    <a href="https://github.com/DaviesGit"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="javascript:void(0)">View Demo</a>
    ·
    <a href="javascript:void(0)">Report Bug</a>
    ·
    <a href="javascript:void(0)">Request Feature</a> -->
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [功能定制](#功能定制)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)
* [免责声明](#免责声明)


<!-- ABOUT THE PROJECT -->
## About The Project

#### 资产管理系统

登录界面

![result00](readme_images/result00.jpg)

添加资产的方式

![result01](readme_images/result01.jpg)

表格导入方式

![result02](readme_images/result02.jpg)

查看所有设备

![result03](readme_images/result03.jpg)

设备信息页面

![result04](readme_images/result04.jpg)

生成设备二维码

![result05](readme_images/result05.jpg)

通过二维码借用的方法

![result06](readme_images/result06.jpg)

后台管理

![result07](readme_images/result07.jpg)



该资产管理系统拥有独创的二维码设备定位技术，可以通过二维码方便的定位对应的设备。该资产管理系统可以支持对资产进行采购、验收、建账、借用、归还、报废、报失等操作。同时支持批量导入和导出操作。网站的静态界面展示：[https://daviesgit.github.io/asset_manager/static/website/login/login.html](https://daviesgit.github.io/asset_manager/static/website/login/login.html)（注意，静态页面并不包含完整功能，如需要使用完整功能，请clone并运行django后端。登录帐号和密码均为admin。）

功能:
* 用户权限管理。
* 设备管理（借用、归还、报废等）。
* 二维码生成与打印。
* 二维码设备快速查找。
* 设备信息的导入导出。

更多信息请参考`资产管理系统主要功能展示.pdf`



### Built With
依赖
* [jQuery](https://jquery.com/)
* [Bootstrap · The most popular HTML, CSS, and JS library in the ...](https://getbootstrap.com/)
* [Python](https://www.python.org/)
* [Django: The Web framework for perfectionists with deadlines](https://www.djangoproject.com/)
* [SQLite](https://www.sqlite.org/)



<!-- GETTING STARTED -->

## Getting Started

这个章节将指导你简单的部署和使用该软件。

### Prerequisites

这个项目的依赖安装步骤在下面给出。

* python3
```sh
sudo apt-get install python3
```

* django
```sh
pip3 install django
```

### Installation

1. Clone the repo
```sh
git clone https://github.com/path/to/the/repository
```

2. 进入到该项目的根目录

<!-- USAGE EXAMPLES -->

## Usage

1. 启动服务器
```sh
python3 manage.py runserver
```

2. 打开浏览器浏览 http://localhost:8000/

## 功能定制

如果需要功能定制，请联系作者 [1182176003@qq.com](1182176003@qq.com)




<!-- ROADMAP -->
## Roadmap

See the [open issues](https://example.com) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Davies - [@qq](1182176003) - 1182176003

Davies - [@email](1182176003@qq.com) - 1182176003@qq.com



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [GitHub](https://github.com/)
* [Font Awesome](https://fontawesome.com)



## 免责声明
* 该软件中所包含的部分内容，包括文字、图片、音频、视频、软件、代码、以及网页版式设计等可能来源于网上搜集。

* 该软件提供的内容仅用于个人学习、研究或欣赏，不可使用于商业和其它意图，一切关于该软件的不正当使用行为均与我们无关，亦不承担任何法律责任。使用该软件应遵守相关法律的规定，通过使用该软件随之而来的风险与我们无关，若使用不当，后果均由个人承担。

* 该软件不提供任何形式的保证。我们不保证内容的正确性与完整性。所有与使用该软件的直接风险均由用户承担。

* 如果您认为该软件中所包含的部分内容侵犯了您的权益，请及时通知我们，我们将尽快予以修正或删除。


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[license-shield]: readme_images/MIT_license.svg
[license-url]: https://opensource.org/licenses/MIT

[product-screenshot]: readme_images/screenshot.png
