/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  images: {
    domains: ["media-exp1.licdn.com", "localhost:8000", "127.0.0.1"],
  },
};

module.exports = nextConfig;
