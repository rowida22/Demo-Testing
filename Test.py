"""a Module to interact with Google PageSpeed Insights API"""
import logging
import urllib.request
import json

class Apispeed():

    def __init__(self, website: str):
        self.__logger = self.__setup_loger()
        self.__logger.info("Initializing the app.")
        url: str = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={}&strategy=desktop&key=AIzaSyCcDNbRIvDPnuOM1TdCwoyzmP6NiGOkcLU".format(website)
        response = urllib.request.urlopen(url)
        self.data = json.loads(response.read())

    def __loadingExperiemnce(self):
        fcp = self.data["loadingExperience"]["metrics"]["FIRST_CONTENTFUL_PAINT_MS"]["category"]
        fid = self.data["loadingExperience"]["metrics"]["FIRST_INPUT_DELAY_MS"]["category"]
        lcp = self.data["loadingExperience"]["metrics"]["LARGEST_CONTENTFUL_PAINT_MS"]["category"]
        cls = self.data["loadingExperience"]["metrics"]["CUMULATIVE_LAYOUT_SHIFT_SCORE"]["category"]
        overall = self.data["loadingExperience"]["overall_category"]
        
        data_LE = {
            "fcp": fcp,
            "fid": fid,
            "lcp": lcp,
            "cls": cls,
            "overall": overall
        }
        return data_LE

    def __originLoadingExperience(self):
        fcp = self.data["originLoadingExperience"]["metrics"]["FIRST_CONTENTFUL_PAINT_MS"]["category"]
        fid = self.data["originLoadingExperience"]["metrics"]["FIRST_INPUT_DELAY_MS"]["category"]
        lcp = self.data["originLoadingExperience"]["metrics"]["LARGEST_CONTENTFUL_PAINT_MS"]["category"]
        cls = self.data["originLoadingExperience"]["metrics"]["CUMULATIVE_LAYOUT_SHIFT_SCORE"]["category"]
        overall = self.data["originLoadingExperience"]["overall_category"]
        
        data_OLE = {
            "fcp":fcp,
            "fid":fid,
            "lcp":lcp,
            "cls":cls,
            "overall":overall
        }
        return data_OLE
        
    def __lighthouseResult(self):    
        fcp = self.data["lighthouseResult"]["audits"]["first-contentful-paint"]["displayValue"]
        tto = self.data["lighthouseResult"]["audits"]["interactive"]["displayValue"]
        lcp = self.data["lighthouseResult"]["audits"]["largest-contentful-paint"]["displayValue"]
        cls = self.data["lighthouseResult"]["audits"]["cumulative-layout-shift"]["displayValue"]
        tbt = self.data["lighthouseResult"]["audits"]["total-blocking-time"]["displayValue"]
        si = self.data["lighthouseResult"]["audits"]["speed-index"]["displayValue"]
        
        data_LHR ={
            "fcp":fcp,
            "tto":tto,
            "lcp":lcp,
            "cls":cls,
            "tbt":tbt,
            "si":si
        }
        return data_LHR

    def __overall(self):    
        overall_performance = self.data["lighthouseResult"]["categories"]["performance"]["score"] * 100

        data_all_performance = {
            "overall_performance": overall_performance
        }
        return data_all_performance

    def get(self):
        data = {
            "loadingExperience":self.__loadingExperiemnce(),
            "originLoadingExperience":self.__originLoadingExperience(),
            "lighthouseResult":self.__lighthouseResult(),
            "overall":self.__overall()
        }
        return data

    @staticmethod
    def __setup_loger():
        """setup the logger
            Log Example:
                2022-05-24 00:45:56,230 - API Speed - INFO: Message
            Returns:
                logging.Logger: logger"""
        logging.basicConfig(
            format='%(asctime)s - %(name)s - %(levelname)s: %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            level=logging.DEBUG,
            filemode="w")
        return logging.getLogger("API Speed")

    def __del__(self):
        del  self.data


if __name__ == "__main__":
    app = Apispeed("https://www.google.com")
    print(app.get())