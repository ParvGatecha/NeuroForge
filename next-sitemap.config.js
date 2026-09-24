/** @type {import('next-sitemap').IConfig} */
const fs = require('fs');
const path = require('path');

module.exports = {
  siteUrl: 'https://tensor-track.vercel.app',
  generateRobotsTxt: true,
  robotsTxtOptions: {
    policies: [
      { userAgent: '*', allow: '/' },
      { userAgent: '*', disallow: '/dashboard' },
      { userAgent: '*', disallow: '/api/' },
    ]
  },
  exclude: [
  '/dashboard',
  '/dashboard/*',
  '/api/*',
  '/admin',
  '/login',
  '/saved-items',
  '/settings',
  ],
  changefreq: 'weekly',
  priority: 0.7,
  additionalPaths: async (config) => {
    const paths = [
      await config.transform(config, '/assessment'),
      await config.transform(config, '/learning-items'),
      await config.transform(config, '/roadmaps'),
    ];

    try {
      const searchIndexPath = path.join(__dirname, 'content/search_index.json');
      if (fs.existsSync(searchIndexPath)) {
        const items = JSON.parse(fs.readFileSync(searchIndexPath, 'utf-8'));
        for (const item of items) {
          if (item && item.slug) {
            paths.push(await config.transform(config, `/learning-items/${item.slug}`));
          }
        }
      }
    } catch (e) {
      console.error('Error generating dynamic sitemap paths', e);
    }

    return paths;
  },
  transform: async (config, pagePath) => {
    // Give higher priority to key pages
    const priorities = {
      '/': 1.0,
      '/assessment': 0.95,
      '/learning-items': 0.9,
      '/roadmaps': 0.9,
    };

    const isLearningItem = pagePath.startsWith('/learning-items/');

    return {
      loc: pagePath,
      changefreq: isLearningItem ? 'monthly' : config.changefreq,
      priority: priorities[pagePath] ?? (isLearningItem ? 0.8 : config.priority),
      lastmod: new Date().toISOString(),
    };
  },
};
