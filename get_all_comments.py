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


def save_csv(list_of_data):
    with open('comments.csv', 'a', encoding='utf-8', newline='') as f:
        w = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        w.writerows([list_of_data])
    f.close()


def get_youtube_comments(key, token, payload=''):
    url = "https://www.youtube.com/youtubei/v1/next"

    querystring = {"key": "AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8", "prettyPrint": "false"}
    cookie = cookies_function(COOKIES)
    if payload == '':
        payload = '{"context":{"client":{"hl":"en","gl":"US","remoteHost":"127.0.0.1","deviceMake":"","deviceModel":"","visitorData":"CgtMaEpscHhCNTVLLyi8yqOSBg%3D%3D","userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36,gzip(gfe)","clientName":"WEB","clientVersion":"2.20220330.06.00","osName":"Windows","osVersion":"10.0","originalUrl":"https://www.youtube.com/watch?v='+key+'","platform":"DESKTOP","clientFormFactor":"UNKNOWN_FORM_FACTOR","configInfo":{"appInstallData":"CLzKo5IGsO-CrgUQt8utBRDCh09FEJjqrQUQ1IOuBRC53f0SEKrCrQUQ2L6tBRCR-PwS"},"userInterfaceTheme":"USER_INTERFACE_THEME_DARK","timeZone":"Africa/Casablanca","browserName":"Chrome","browserVersion":"99.0.4844.84","screenWidthPoints":942,"screenHeightPoints":961,"screenPixelDensity":1,"screenDensityFloat":1,"utcOffsetMinutes":0,"connectionType":"CONN_CELLULAR_4G","memoryTotalKbytes":"8000000","mainAppWebInfo":{"graftUrl":"https://www.youtube.com/watch?v='+key+'","pwaInstallabilityStatus":"PWA_INSTALLABILITY_STATUS_CAN_BE_INSTALLED","webDisplayMode":"WEB_DISPLAY_MODE_BROWSER","isWebNativeShareAvailable":true}},"user":{"lockedSafetyMode":false},"request":{"useSsl":true,"internalExperimentFlags":[],"consistencyTokenJars":[{"encryptedTokenJarContents":"AGDxDeMQHdAcXn03szZTbSC7Wdd5xSBCG6OrYHvyE_dQCYFXHLzymMkCtBU28LLgjED70-VJEvtHXX92LgEZiWZI99IMHaE0ErXP3UESo35dOOamSAhjuRlvMUUPh-w7xSHtI0YFrutN43-rDkrWQZ_o","expirationSeconds":"600"}]},"clickTracking":{"clickTrackingParams":"CLoCELsvGAIiEok-ufzjzPb2AhVOOOAKHecnDrU="},"adSignalsInfo":{"params":[{"key":"dt","value":"1648933445997"},{"key":"flash","value":"0"},{"key":"frm","value":"0"},{"key":"u_tz","value":"0"},{"key":"u_his","value":"4"},{"key":"u_h","value":"1080"},{"key":"u_w","value":"1920"},{"key":"u_ah","value":"1032"},{"key":"u_aw","value":"1920"},{"key":"u_cd","value":"24"},{"key":"bc","value":"31"},{"key":"bih","value":"961"},{"key":"biw","value":"926"},{"key":"brdim","value":"0,0,0,0,1920,0,1920,1032,942,961"},{"key":"vis","value":"1"},{"key":"wgl","value":"true"},{"key":"ca_type","value":"image"}],"bid":"ANyPxKpS_G8YSUkiGNbLjKUPiIXExLLDCALK-N4poqAciPYZC2Qr4Z0XQvjWjQoIst9PoxOk9Ytf3ofQliIHpsNlKc-U0UNGpA"}},"continuation":"' + token + '"}'
    headers = {
        'sec-ch-ua': "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"99\", \"Google Chrome\";v=\"99\"",
        'x-origin': "https://www.youtube.com",
        'authorization': "SAPISIDHASH 1648944465_44080a4a202eb69b48761494206595da7c15bca6",
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
        'x-youtube-client-version': "2.20220324.01.00",
        'content-type': "application/json",
        'x-goog-visitor-id': "CgtMaEpscHhCNTV3ayi8yqOSBg%3D%3D",
        'accept': "*/*",
        'cache-control': "no-cache"
    }

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring, cookies=cookie)

    return response.json()


def worker(token, watch_id, title):
    response = get_youtube_comments(watch_id, token)
    # print(response)
    try:
        response_p = response['onResponseReceivedEndpoints'][0]['appendContinuationItemsAction']['continuationItems']
    except:
        response_p = response['onResponseReceivedEndpoints'][1]['reloadContinuationItemsCommand']['continuationItems']
    for i in range(0, len(response_p)):
        comment = response_p[i]

        if i == len(response_p) - 1:
            try:
                token = comment['commentThreadRenderer']['continuationEndpoint']['continuationCommand']['token']
            except:
                token = comment['continuationItemRenderer']['continuationEndpoint']['continuationCommand']['token']

            print(f'token: {token}')
            return worker(token, watch_id, title)

        try:
            comment_text = comment['commentThreadRenderer']['comment']['commentRenderer']['contentText']['runs']
            full_comment = ''
            for comment_ in comment_text:
                full_comment = ''.join(comment_['text'])
            # if '"' in full_comment:
            save_csv([watch_id, title, full_comment])
        except:
            pass


def first_req(watch_id, title):
    payload = '{"context":{"client":{"hl":"en","gl":"US","remoteHost":"10.10.10.10","deviceMake":"","deviceModel":"","visitorData":"CgtkMaEiscHhCNTV3ayjnj_0yRBga%3D%3D","userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36,gzip(gfe)","clientName":"WEB","clientVersion":"2.20220325.00.00","osName":"Windows","osVersion":"10.0","originalUrl":"https://www.youtube.com/watch?v=' + watch_id + '","platform":"DESKTOP","clientFormFactor":"UNKNOWN_FORM_FACTOR","configInfo":{"appInstallData":"COeP_JEGEPCCrgUQt8utBRD_960FEJjqrQUQ1ILuTRCc2f0SENi-rQUQkfj8Eg%3D%3D"},"userInterfaceTheme":"USER_INTERFACE_THEME_DARK","timeZone":"Africa/Casablanca","browserName":"Chrome","browserVersion":"99.0.4844.82","screenWidthPoints":1920,"screenHeightPoints":150,"screenPixelDensity":1,"screenDensityFloat":1,"utcOffsetMinutes":60,"memoryTotalKbytes":"8000000","clientScreen":"WATCH","mainAppWebInfo":{"graftUrl":"https://www.youtube.com/watch?v=' + watch_id + '","pwaInstallabilityStatus":"PWA_INSTALLABILITY_STATUS_CAN_BE_INSTALLED","webDisplayMode":"WEB_DISPLAY_MODE_BROWSER","isWebNativeShareAvailable":true}},"user":{"lockedSafetyMode":false},"request":{"useSsl":true,"internalExperimentFlags":[],"consistencyTokenJars":[]},"clickTracking":{"clickTrackingParams":"COgCENwwIhMI2pj4suTj9gIVxYtVCh1vJgCTMgpnLWhpZ2gtcmVjWg0oRXdoYXRfdG9fd2F0Y2iaAQYQjh4YngE="},"adSignalsInfo":{"params":[{"key":"dt","value":"1648207161327"},{"key":"flash","value":"0"},{"key":"frm","value":"0"},{"key":"u_tz","value":"60"},{"key":"u_his","value":"2"},{"key":"u_h","value":"1080"},{"key":"u_w","value":"1920"},{"key":"u_ah","value":"1032"},{"key":"u_aw","value":"1920"},{"key":"u_cd","value":"24"},{"key":"bc","value":"31"},{"key":"bih","value":"150"},{"key":"biw","value":"1904"},{"key":"brdim","value":"0,0,0,0,1920,1,1920,1032,1920,150"},{"key":"vis","value":"1"},{"key":"wgl","value":"true"},{"key":"ca_type","value":"image"}],"bid":"ANyPxKrKY_58mXfqN8sdQXuzFqxwRsnueTDrDQNCA-DhJdmLpt5wp30eClsa7bTokZRS1ET_IY-km55khP3IuaRnuOEnJagl0w"}},"videoId":"' + watch_id + '","racyCheckOk":false,"contentCheckOk":false,"autonavState":"STATE_ON","playbackContext":{"vis":0,"lactMilliseconds":"-1"},"captionsRequested":false}'
    response = get_youtube_comments(watch_id, '', payload)
    response_p = response['contents']['twoColumnWatchNextResults']['results']['results']['contents']
    token = response_p[len(response_p) - 1]['itemSectionRenderer']['contents'][0]['continuationItemRenderer'][
        'continuationEndpoint']['continuationCommand']['token']
    print(f'token {token}')
    return worker(token, video_id, title)


if __name__ == '__main__':
    data = []
    with open('videos.csv', 'r', encoding='utf-8', newline='') as f:
        r = csv.reader(f, delimiter=',', quotechar='"')
        for row in r:
            data.append(row)
    f.close()
    for d in data:
        try:
            video_id, title = d
            print(d)
            first_req(video_id, title)
        except Exception as e:
            print(f'error: {e}')
