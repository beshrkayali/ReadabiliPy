from ..readabilipy.extractors.extract_title import extract_title
from ..readabilipy.extractors.extract_byline import extract_byline


def test_extract_title():
    htmls = [
        """
            <html>
            <head>
                <meta name="fb_title" content="Example title" />
            </head>
            <body>
                <p>Hello world</p>
            <body>
            </html>
        """,
        """
            <html>
            <head>
            </head>
            <body>
                <h2 class="title">Silly title</h2>
                <h1 class="title">Bad title</h1>
                <header><h1>Example title</h1></header>
                <p>Hello world</p>
            <body>
            </html>
        """,
        """
            <html>
            <head>
            </head>
            <body>
                <h2 itemprop="headline">Example title</h2>
                <header><h1>Incorrect title</h1></header>
                <p>Hello world</p>
            <body>
            </html>
        """
    ]
    addicting_info_htmls = [
        """
            <h1 class="entry-title">
                <a href="http://addictinginfo.com/2018/10/15/trump-denies-charitable-donation-he-promised-if-elizabeth-warren-releases-dna-results-and-its-on-video/"
                    title="Permalink to Trump Denies Charitable Donation He Promised If Elizabeth Warren Releases DNA Results And It&#8217;s On Video"
                    rel="bookmark">Trump Denies Charitable Donation He Promised If Elizabeth Warren Releases DNA Results And
                    It&#8217;s On Video</a>
            </h1>
        """,
        """
            <meta property="og:title" content="Trump Denies Charitable Donation He Promised If Elizabeth Warren Releases DNA Results And It&#8217;s On Video" />
        """
    ]
    for html in htmls:
        output = extract_title(html)
        expected_output = "Example title"
        assert output == expected_output
    for html in addicting_info_htmls:
        output = extract_title(html)
        expected_output = "Trump Denies Charitable Donation He Promised If Elizabeth Warren Releases DNA Results And It’s On Video"
        assert output == expected_output


def test_extract_byline():

    htmls = [
        """
            <meta name="author" content="Ed Chalstrey" />
        """
    ]

    for html in htmls:
        output = extract_byline(html)
        expected_output = "Ed Chalstrey"
        assert output == expected_output
