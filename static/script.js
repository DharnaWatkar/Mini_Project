function previewImage(event) {
    // Get the uploaded image file
    const file = event.target.files[0];
    
    // Show the uploaded image
    const reader = new FileReader();
    reader.onload = function () {
      const imgElement = document.getElementById("uploadedImage");
      imgElement.src = reader.result;
      imgElement.style.display = "block"; // Display image after upload
    };
    
    if (file) {
      reader.readAsDataURL(file);  // Convert the image to base64
    }
  }
  
  function scanFingerprint() {
    // Get the image file from the input element
    const fileInput = document.getElementById("fingerprintUpload");
    const file = fileInput.files[0];
  
    if (!file) {
      alert("Please upload a fingerprint image first.");
      return;
    }
  
    // Create a FormData object to send the image file
    const formData = new FormData();
    formData.append("file", file);
  
    // Make a POST request to the Flask API
    fetch("http://127.0.0.1:5000/predict", {
      method: "POST",
      body: formData,
    })
      .then((response) => response.json())
      .then((data) => {
        // Handle the response
        if (data.prediction) {
          const resultText = `Predicted Blood Group: ${data.prediction}`;
          document.getElementById("result").innerText = resultText;
        } else {
          document.getElementById("result").innerText = "Error: " + data.error;
        }
      })
      .catch((error) => {
        console.error("Error:", error);
        document.getElementById("result").innerText = "An error occurred during the scan.";
      });
  }
  