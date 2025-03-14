FROM node:18.20

# Install system dependencies
RUN apt-get update && \
    apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /var/www/blog-frontend

COPY blog-frontend/package*.json ./
# Cài đặt các dependencies
RUN npm install

# Thêm sở hữu cho node_modules để tránh lỗi quyền
RUN chown -R node:node node_modules

# Copy toàn bộ mã nguồn vào container
COPY . .

# Chỉ định cổng sẽ expose
EXPOSE 3000

# Thiết lập biến môi trường
ENV NODE_ENV development

# Khởi động ứng dụng
CMD ["npm", "run", "dev"]