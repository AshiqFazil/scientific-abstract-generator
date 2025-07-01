document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("generateForm");
    const loader = document.getElementById("loader");
    const resultSection = document.getElementById("resultSection");
    const abstractText = document.getElementById("generatedAbstract");
    const copyBtn = document.getElementById("copyBtn");
    const wordCountDisplay = document.getElementById("wordCount");

    loader.style.display = "none";
    resultSection.style.display = "none";

    form.addEventListener("submit", async function (e) {
        e.preventDefault(); // prevent normal form submit

        const title = document.getElementById("title").value;
        const keywords = document.getElementById("keywords").value;
        const domain = document.getElementById("domain").value;

        loader.style.display = "inline-block"; 
        resultSection.style.display = "none";

        try {
            const response = await fetch("/generate", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ title, keywords, domain })
            });

            const data = await response.json();

            if (data.abstract) {
                abstractText.innerText = data.abstract;
                resultSection.style.display = "block";

                const words = data.abstract.trim().split(/\s+/).length;
                wordCountDisplay.innerText = `Word count: ${words}`;
            } else {
                abstractText.innerText = "Failed to generate abstract.";
                resultSection.style.display = "block";
            }
        } catch (error) {
            console.error(error);
            abstractText.innerText = "Error connecting to server.";
            resultSection.style.display = "block";
        } finally {
            loader.style.display = "none";
        }
    });

    copyBtn?.addEventListener("click", function () {
        const text = abstractText.innerText;
        navigator.clipboard.writeText(text).then(() => {
            copyBtn.innerText = "Copied!";
            setTimeout(() => copyBtn.innerText = "Copy", 1500);
        }).catch(() => {
            copyBtn.innerText = "Failed!";
        });
    });
});
