from playwright.sync_api import sync_playwright
import os

def html_to_pdf(html_path, output_pdf_path):
    """将HTML文件转换为PDF，保留所有视觉效果"""
    
    # 获取HTML文件的绝对路径
    html_abs_path = os.path.abspath(html_path)
    html_dir = os.path.dirname(html_abs_path)
    html_file = f"file:///{html_abs_path.replace(os.sep, '/')}"
    
    print(f"正在加载: {html_file}")
    
    with sync_playwright() as p:
        # 启动浏览器
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={'width': 1920, 'height': 1080})
        
        # 导航到HTML文件
        page.goto(html_file, wait_until='networkidle')
        
        # 等待一下，确保所有资源加载完成
        page.wait_for_timeout(2000)
        
        # 生成PDF
        page.pdf(
            path=output_pdf_path,
            format='A4',
            print_background=True,
            margin={
                'top': '0.5in',
                'right': '0.5in',
                'bottom': '0.5in',
                'left': '0.5in'
            }
        )
        
        browser.close()
        print(f"PDF已生成: {output_pdf_path}")

if __name__ == "__main__":
    html_path = "index.html"
    output_pdf_path = "杨紫瑶_AI产品经理作品集.pdf"
    
    try:
        html_to_pdf(html_path, output_pdf_path)
        print("\n✅ PDF生成成功！")
    except Exception as e:
        print(f"\n❌ 错误: {e}")
        print("\n提示: 如果第一次运行，请先安装playwright:")
        print("  pip install playwright")
        print("  playwright install chromium")
