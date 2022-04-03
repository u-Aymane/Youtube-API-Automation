import csv
import requests
import json

COOKIES = json.loads(open('variables.json', 'r').read())['COOKIES']

def cookies_function(text):
    parts = text.split('; ')
    ans = {}
    for i in parts:
        ans[i.split('=', 1)[0]] = i.split('=', 1)[1]

    return ans


def list_videos():
    url = "https://www.youtube.com/youtubei/v1/search"

    querystring = {"key": "AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8", "prettyPrint": "false"}
    cookie = cookies_function(COOKIES)
    payload = '{"context":{"client":{"hl":"en","gl":"US","remoteHost":"127.0.0.1","deviceMake":"","deviceModel":"","visitorData":"CgtMaEpscHhCNTV3awiTmvyRBg%3D%3D","userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36,gzip(gfe)","clientName":"WEB","clientVersion":"2.20220325.00.00","osName":"Windows","osVersion":"10.0","originalUrl":"https://www.youtube.com/results?search_query='+search_val+'","platform":"DESKTOP","clientFormFactor":"UNKNOWN_FORM_FACTOR","configInfo":{"appInstallData":"CJOa_JEGELfLrQUQ__etBRDUg64FEJjqrQUQwIKuBRCc2f0SEJH4_BIQ2L6tBQ%3D%3D"},"userInterfaceTheme":"USER_INTERFACE_THEME_DARK","timeZone":"Africa/Casablanca","browserName":"Chrome","browserVersion":"99.0.4844.82","screenWidthPoints":1920,"screenHeightPoints":431,"screenPixelDensity":1,"screenDensityFloat":1,"utcOffsetMinutes":60,"memoryTotalKbytes":"8000000","mainAppWebInfo":{"graftUrl":"/results?search_query='+search_val+'","pwaInstallabilityStatus":"PWA_INSTALLABILITY_STATUS_CAN_BE_INSTALLED","webDisplayMode":"WEB_DISPLAY_MODE_BROWSER","isWebNativeShareAvailable":true}},"user":{"lockedSafetyMode":false},"request":{"useSsl":true,"internalExperimentFlags":[],"consistencyTokenJars":[]},"clickTracking":{"clickTrackingParams":"CB4Q7VAiEwiV0Iql6eP2AhXckFUKHYyqCeM="},"adSignalsInfo":{"params":[{"key":"dt","value":"1648299983364"},{"key":"flash","value":"0"},{"key":"frm","value":"0"},{"key":"u_tz","value":"60"},{"key":"u_his","value":"3"},{"key":"u_h","value":"1080"},{"key":"u_w","value":"1920"},{"key":"u_ah","value":"1032"},{"key":"u_aw","value":"1920"},{"key":"u_cd","value":"24"},{"key":"bc","value":"31"},{"key":"bih","value":"431"},{"key":"biw","value":"1904"},{"key":"brdim","value":"0,0,0,0,1920,0,1920,1032,1920,431"},{"key":"vis","value":"1"},{"key":"wgl","value":"true"},{"key":"ca_type","value":"image"}],"bid":"ANyPxKr9soo70g5hss9iaLt-s_N8j6vllaa9b37X83DNmtpnpwZc3C0rPIeSMc29E-a5cU9T2ppdWjM2vAn6f4sClvun3bwFfA"}},"query":"'+search_val+'","webSearchboxStatsUrl":"/search?oq='+search_val+'&gs_l=youtube.3..0i71k1l10.0.0.1.115475.0.0.0.0.0.0.0.0..0.0.ytpmucmn17_e,ytpo-bo-me=1,ytpo-bo-uco-e=1,ytpo-bo-uco-mv=17,cfro=1,ytpo-bo-me=0...0...1ac..64.youtube..0.0.0....0.gexuupbgu9k"}'
    headers = {
        'sec-ch-ua': "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"99\", \"Google Chrome\";v=\"99\"",
        'x-origin': "https://www.youtube.com",
        'authorization': "SAPISIDHASH 1648299519_dd5dd0cafa1bc6cf3402f12b2767cd612e099d2f",
        'sec-ch-ua-arch': "\"x86\"",
        'sec-ch-ua-platform-version': "\"14.0.0\"",
        'x-goog-authuser': "0",
        'sec-ch-ua-full-version-list': "\" Not A;Brand\";v=\"99.0.0.0\", \"Chromium\";v=\"99.0.4844.82\", \"Google Chrome\";v=\"99.0.4844.82\"",
        'sec-ch-ua-platform': "\"Windows\"",
        'sec-ch-ua-bitness': "\"64\"",
        'sec-ch-ua-mobile': "?0",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36",
        'sec-ch-ua-full-version': "\"99.0.4844.82\"",
        'x-youtube-client-name': "1",
        'x-youtube-client-version': "2.20220325.00.00",
        'content-type': "application/json",
        'x-goog-visitor-id': "CgtMaEpscHhCNTV3kyiTmvyRBg%3D%3D",
        'accept': "*/*",
        'cache-control': "no-cache"
    }

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring, cookies=cookie)

    return response.json()


def worker(token, search_keyword):
    url = "https://www.youtube.com/youtubei/v1/search"

    querystring = {"key": "AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8", "prettyPrint": "false"}
    cookie = cookies_function(COOKIES)
    payload = '{"context":{"client":{"hl":"en","gl":"US","remoteHost":"127.0.0.1","deviceMake":"","deviceModel":"","visitorData":"CgtMaEpscHhCNTV3ayjoofyRBg%3D%3D","userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36,gzip(gfe)","clientName":"WEB","clientVersion":"2.20220325.00.00","osName":"Windows","osVersion":"10.0","originalUrl":"https://www.youtube.com/results?search_query='+search_keyword+'","platform":"DESKTOP","clientFormFactor":"UNKNOWN_FORM_FACTOR","configInfo":{"appInstallData":"COih_JEGEP_3rQUQ8IKuBRDUg64FEJjqrQUQt8utBRCc2f0SENi-rQUQkfj8Eg%3D%3D"},"userInterfaceTheme":"USER_INTERFACE_THEME_DARK","timeZone":"Africa/Casablanca","browserName":"Chrome","browserVersion":"99.0.4844.82","screenWidthPoints":1920,"screenHeightPoints":431,"screenPixelDensity":1,"screenDensityFloat":1,"utcOffsetMinutes":60,"connectionType":"CONN_CELLULAR_4G","memoryTotalKbytes":"8000000","mainAppWebInfo":{"graftUrl":"https://www.youtube.com/results?search_query='+search_keyword+'","pwaInstallabilityStatus":"PWA_INSTALLABILITY_STATUS_CAN_BE_INSTALLED","webDisplayMode":"WEB_DISPLAY_MODE_BROWSER","isWebNativeShareAvailable":true}},"user":{"lockedSafetyMode":false},"request":{"useSsl":true,"internalExperimentFlags":[],"consistencyTokenJars":[]},"clickTracking":{"clickTrackingParams":"CCEQui8iEwjEm86q7eP2AhWP0lUKHUHiB8s="},"adSignalsInfo":{"params":[{"key":"dt","value":"1648300264644"},{"key":"flash","value":"0"},{"key":"frm","value":"0"},{"key":"u_tz","value":"60"},{"key":"u_his","value":"5"},{"key":"u_h","value":"1080"},{"key":"u_w","value":"1920"},{"key":"u_ah","value":"1032"},{"key":"u_aw","value":"1920"},{"key":"u_cd","value":"24"},{"key":"bc","value":"31"},{"key":"bih","value":"431"},{"key":"biw","value":"1904"},{"key":"brdim","value":"0,0,0,0,1920,0,1920,1032,1920,431"},{"key":"vis","value":"1"},{"key":"wgl","value":"true"},{"key":"ca_type","value":"image"}],"bid":"ANyPxKqEC-2pStDoiJvGjS3e6NsIyhhePYho1YrbN-x6aGrXgctPWXYTqCajIYGAcayWNhOL6MnYjGHWPm6F9CHnvcWorRKEcA"}},"continuation":"'+token+'"}'
    headers = {
        'sec-ch-ua': "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"99\", \"Google Chrome\";v=\"99\"",
        'x-origin': "https://www.youtube.com",
        'authorization': "SAPISIDHASH 1648301371_edcabb43e61f5ced8680989780742f8f24ca900c",
        'sec-ch-ua-arch': "\"x86\"",
        'sec-ch-ua-platform-version': "\"14.0.0\"",
        'x-goog-authuser': "0",
        'sec-ch-ua-full-version-list': "\" Not A;Brand\";v=\"99.0.0.0\", \"Chromium\";v=\"99.0.4844.82\", \"Google Chrome\";v=\"99.0.4844.82\"",
        'sec-ch-ua-platform': "\"Windows\"",
        'sec-ch-ua-bitness': "\"64\"",
        'sec-ch-ua-mobile': "?0",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36",
        'sec-ch-ua-full-version': "\"99.0.4844.82\"",
        'x-youtube-client-name': "1",
        'x-youtube-client-version': "2.20220325.00.00",
        'content-type': "application/json",
        'x-goog-visitor-id': "CgtMaEpscHfCNTV3ayjoofyRBg%3D%3D",
        'accept': "*/*",
        'cache-control': "no-cache"
    }

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring, cookies=cookie)

    return response.json()


def save_csv(list_of_data):
    with open('videos.csv', 'a', encoding='utf-8', newline='') as f:
        w = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        w.writerows([list_of_data])
    f.close()


def save_search(token):
    data = worker(token, search_val)
    root = data['onResponseReceivedCommands'][0]['appendContinuationItemsAction']['continuationItems'][0][
        'itemSectionRenderer']['contents']
    token = data['onResponseReceivedCommands'][0]['appendContinuationItemsAction']['continuationItems']
    token_text = token[len(token) - 1]['continuationItemRenderer']['continuationEndpoint']['continuationCommand'][
        'token']
    for content in root:
        if 'videoRenderer' in content.keys():
            video_id = content['videoRenderer']['videoId']
            title = content['videoRenderer']['title']['runs'][0]['text']
            save_csv([video_id, title])
    print(f'token: {token_text}')
    return save_search(token_text)


def first_save_search():
    data = list_videos()
    root = data['contents']['twoColumnSearchResultsRenderer']['primaryContents']['sectionListRenderer']['contents'][0][
        'itemSectionRenderer']['contents']
    token = data['contents']['twoColumnSearchResultsRenderer']['primaryContents']['sectionListRenderer']['contents']
    token_text = token[len(token) - 1]['continuationItemRenderer']['continuationEndpoint']['continuationCommand'][
        'token']
    for content in root:
        if 'videoRenderer' in content.keys():
            video_id = content['videoRenderer']['videoId']
            title = content['videoRenderer']['title']['runs'][0]['text']
            save_csv([video_id, title])

    return save_search(token_text)


if __name__ == '__main__':
    search_val = input('Search Keyword: ').replace(' ', '+')
    try:
        first_save_search()
    except:
        print('PLEASE VERIFY YOUR COOKIES!')