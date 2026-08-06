from abc import ABCMeta, abstractmethod

class Report(metaclass=ABCMeta):
    @abstractmethod
    def generate_report(self, v):
        ...

class TextReport(Report):
    def __init__(self, date, name):
        self.date = date
        self.name = name

    def generate_report(self, visitor):
        visitor.generate_report(self)

class ImageReport(Report):
    def __init__(self, date, name, images):
        self.date = date
        self.name = name
        self.images = images

    def generate_report(self, visitor):
        visitor.generate_report(self)

class GraphReport(Report):
    def __init__(self, date, name, graphs):
        self.date = date
        self.name = name
        self.graphs = graphs

    def generate_report(self, visitor):
        visitor.generate_report(self)

class ReportGenerator(metaclass=ABCMeta):
    @abstractmethod
    def generate_report(self, txt_report: TextReport):
        ...

    @abstractmethod
    def generate_report(self, img_report: ImageReport):
        ...

    @abstractmethod
    def generate_report(self, grp_report: GraphReport):
        ...

class PDFGenerator(ReportGenerator):
    def generate_report(self, txt_report: TextReport):
        print(f"Generating PDF report from TextReport: {txt_report.name}.pdf")

    def generate_report(self, img_report: ImageReport):
        print(f"Generating PDF report from image report: {img_report.name}.pdf")

    def generate_report(self, grp_report: GraphReport):
        print(f"Generating PDF report from graph report: {grp_report.name}.pdf")

class XlsGenerator(ReportGenerator):
    def generate_report(self, txt_report: TextReport):
        print(f"Generating xls report from TextReport: {txt_report.name}.xls")

    def generate_report(self, img_report: ImageReport):
        print(f"Generating xls report from image report: {img_report.name}.xls")

    def generate_report(self, grp_report: GraphReport):
        print(f"Generating xls report from graph report: {grp_report.name}.xls")

class HTMLGenerator(ReportGenerator):
    def generate_report(self, txt_report: TextReport):
        print(f"Generating html report from TextReport: {txt_report.name}.html")

    def generate_report(self, img_report: ImageReport):
        print(f"Generating html report from image report: {img_report.name}.html")

    def generate_report(self, grp_report: GraphReport):
        print(f"Generating html report from graph report: {grp_report.name}.html")

def main():
    reportA = ImageReport("Hoje", "Relatório A", [1, 2, 3])
    
    PDF_builder = PDFGenerator()
    HTML_builder = HTMLGenerator()
    Xls_builder = XlsGenerator()

    reportA.generate_report(PDF_builder)
    reportA.generate_report(HTML_builder)

    reportB = TextReport("Hoje", "Relatório 2")
    
    reportB.generate_report(Xls_builder)

if __name__ == "__main__":
    main()
