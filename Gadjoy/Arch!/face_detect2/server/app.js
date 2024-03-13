const express = require('express');
const multer = require('multer');
const cors = require('cors');

const app = express();
const port = 5000;

// Middleware for handling CORS
app.use(cors());

// Middleware for handling file uploads
const storage = multer.memoryStorage();
const upload = multer({ storage: storage });

// Handle the file upload endpoint
app.post('/process_image', upload.single('uploadedImage'), (req, res) => {
  try {
    const originalBuffer = req.file.buffer; // Assuming the uploaded file is in memory

    // Encode the image data to base64
    const base64EncodedData = originalBuffer.toString('base64');

    // Process the uploaded file (you can replace this with your facial landmark detection logic)
    const result = {
      message: 'Image processing successful!',
      processed_image: base64EncodedData, // You can send this back to the client if needed
    };

    res.header('Access-Control-Allow-Origin', 'http://127.0.0.1:8080'); // Adjust the port if needed
    res.json(result);
  } catch (error) {
    console.error('Error processing image:', error);
    res.status(500).json({ message: 'Image processing failed. Please try again.' });
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
