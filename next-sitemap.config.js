/** @type {import('next-sitemap').IConfig} */
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
    return [
      await config.transform(config, '/learning-items'),
    ];
  },
  transform: async (config, path) => {
    // Give higher priority to key pages
    const priorities = {
      '/': 1.0,
      '/learning-items': 0.9,
      '/roadmap': 0.9,
      '/roadmaps': 0.9,
    };
    return {
      loc: path,
      changefreq: config.changefreq,
      priority: priorities[path] ?? config.priority,
      lastmod: new Date().toISOString(),
    };
  },
};
