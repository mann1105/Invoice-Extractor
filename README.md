<h1>PDF to JSON Extractor</h1>

<p>This project enables extract crucial invoice information from PDF documents and convert it into structured JSON format. With the capabilities of Large Language Model (LLM) the app intelligently analyzes the content and organizes the extracted data, ensuring effortless downstream processing and integration.</p>

<h2>🚀 Key Features</h2>

<ul>
    <li><strong>Multi-File Processing:</strong> Upload and process multiple PDF invoices simultaneously.</li>
    <li><strong>Information Extraction:</strong> Employs Google's gemini LLM API to accurately identify and extract relevant invoice details.</li>
    <li><strong>JSON Output:</strong> Presents the extracted data in a well-structured JSON format.</li>
    <li><strong>Download option:</strong> Provides the option to download JSON data for each processed invoice separately.</li>
    <li><strong>User-Friendly Interface:</strong> Offers a clear interface.</li>
</ul>

<h2>🛠️ Installation & Setup</h2>

<ol>
    <li>Ensure you have Python installed on your system.</li>
    <li>Clone this repository: <code>git clone https://github.com/mann1105/Invoice-Extractor.git</code></li
    <li>Install the required dependencies: <code>pip install -r requirements.txt</code></li>
    <li>Set up your Gemini API key:
        <ul>
            <li>Create a <code>.env</code> file in the project root.</li>
            <li>Add the following line to the <code>.env</code> file, replacing 'your-api-key' with your actual Gemini API key: <code>GOOGLE_API_KEY=your-api-key</code></li>
        </ul>
    </li>
    <li>Run the Streamlit app: <code>streamlit run app.py</code></li>
</ol>

<h2>📚 Dependencies</h2>

<ul>
    <li><code>python-dotenv</code></li>
    <li><code>langchain</code></li>
    <li><code>langchain-community</code></li>
    <li><code>langchain-google-genai</code></li>
    <li><code>sentence-transformers</code></li>
    <li><code>pypdf</code></li>
    <li><code>streamlit</code></li>
</ul>

<h2>📄 Usage</h2>

<ol>
    <li><strong>Upload PDFs:</strong> Utilize the file uploader in the sidebar to select one or multiple PDF invoice files.</li>
    <li><strong>Extract Data:</strong> Click the "Extract Data" button to initiate the extraction process.</li>
    <li><strong>Review & Download:</strong> 
        <ul>
            <li>Expand each invoice section to view the extracted JSON data.</li>
            <li>Click the "Download JSON" button to save the JSON data for each invoice individually.</li>
        </ul>
    </li>
    <li><strong>Clear Files:</strong> Click the "Clear Files" button to reset the app and upload new files.</li>
</ol>

<h2>Demo Video</h2>
<li><a href="https://drive.google.com/file/d/1VvoKNwKQbGE7pq329yjCkbA2xF6h8NKH/view?usp=sharing">Pdf to JSON extractor</a></li>

</body>
</html>
