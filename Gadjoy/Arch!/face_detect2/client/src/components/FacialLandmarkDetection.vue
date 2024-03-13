<template>
  <div id="facial-landmark-detection" class="center">
    <header>
      <h1>Facial Landmark Detection</h1>
    </header>

    <main>
      <table>
        <tr>
          <td>
            <input type="file" accept=".jpg" @change="handleImageUpload" />
          </td>
          <td>
            <button @click="uploadImage">Upload</button>
          </td>
          <td>
            <button @click="fetchResultImage" :disabled="!result">
              Fetch Result
            </button>
          </td>
        </tr>
      </table>

      <div v-if="status !== null" class="status">
        {{ status }}
      </div>

      <canvas v-if="result" ref="outputCanvas" width="600" height="400"></canvas>

      <div v-if="result" class="result-image-container">
        <img :src="result" alt="Result Image" />
      </div>

      <!-- Include HelloWorld.vue component -->
      <HelloWorld />
    </main>

    <footer>
      <p>&copy; 2024 Facial Landmark Detection</p>
    </footer>
  </div>
</template>

<script>
import HelloWorld from './HelloWorld.vue'; // Import HelloWorld.vue

export default {
  components: {
    HelloWorld, // Register HelloWorld component
  },
  data() {
    return {
      status: null,
      result: null,
      imageFile: null,
      uploadedImage: null,
    };
  },
  methods: {
    handleImageUpload(event) {
      this.status = null;
      this.result = null;
      this.uploadedImage = null;

      const input = event.target;
      const file = input.files[0];

      if (file) {
        const reader = new FileReader();
        reader.onload = (e) => {
          this.uploadedImage = e.target.result;
        };
        reader.readAsDataURL(file);
        this.imageFile = file;
      }
    },
    async uploadImage() {
      if (!this.imageFile) {
        this.status = "Please select an image file.";
        return;
      }

      const formData = new FormData();
      formData.append("uploadedImage", this.uploadedImage); // Use the correct key for image data

      try {
        const uploadResponse = await fetch("http://127.0.0.1:5000/process_image", {
          method: "POST",
          body: formData,
        });

        if (uploadResponse.ok) {
          this.status = "Image upload successful!";
          await this.fetchResultImage(); // Automatically fetch result after successful upload
        } else {
          const errorData = await uploadResponse.json();
          this.status = `Error uploading image: ${errorData.message}`;
        }
      } catch (error) {
        console.error("Error uploading image:", error);
        this.status = "Image upload failed. Please try again.";
      }
    },
    async fetchResultImage() {
      try {
        const response = await fetch("http://127.0.0.1:5000/get_processed_image");
        if (response.ok) {
          const resultData = await response.json();
          this.result = resultData.processed_image;
        } else {
          this.status = "Error fetching result image.";
        }
      } catch (error) {
        console.error("Error fetching result image:", error);
        this.status = "Error fetching result image. Please try again.";
      }
    },
  },
};
</script>

<style>
/* Add your CSS styling here */
body, html {
  height: 100%;
  margin: 0;
}

#facial-landmark-detection {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100%;
}

header {
  background-color: #333;
  color: #fff;
  text-align: center;
  padding: 10px;
}

footer {
  background-color: #333;
  color: #fff;
  text-align: center;
  padding: 10px;
  position: fixed;
  bottom: 0;
  width: 100%;
}

main {
  margin: 20px;
}

table {
  margin-bottom: 20px;
}

.status {
  margin-top: 10px;
  padding: 10px;
  border: 1px solid #ccc;
  background-color: #f0f0f0;
}

.result-image-container {
  margin-top: 20px;
  text-align: center;
}

.result-image-container img {
  max-width: 100%;
  height: auto;
}
</style>
