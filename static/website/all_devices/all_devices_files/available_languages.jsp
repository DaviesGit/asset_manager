










AUI.add(
	'portal-available-languages',
	function(A) {
		var available = {};

		var direction = {};

		

			available['ca_ES'] = '加泰罗尼亚文 (西班牙)';
			direction['ca_ES'] = 'ltr';

		

			available['zh_CN'] = '中文 (中国)';
			direction['zh_CN'] = 'ltr';

		

			available['en_US'] = '英文 (美国)';
			direction['en_US'] = 'ltr';

		

			available['fi_FI'] = '芬兰文 (芬兰)';
			direction['fi_FI'] = 'ltr';

		

			available['fr_FR'] = '法文 (法国)';
			direction['fr_FR'] = 'ltr';

		

			available['de_DE'] = '德文 (德国)';
			direction['de_DE'] = 'ltr';

		

			available['iw_IL'] = '希伯来文 (以色列)';
			direction['iw_IL'] = 'rtl';

		

			available['hu_HU'] = '匈牙利文 (匈牙利)';
			direction['hu_HU'] = 'ltr';

		

			available['ja_JP'] = '日文 (日本)';
			direction['ja_JP'] = 'ltr';

		

			available['pt_BR'] = '葡萄牙文 (巴西)';
			direction['pt_BR'] = 'ltr';

		

			available['es_ES'] = '西班牙文 (西班牙)';
			direction['es_ES'] = 'ltr';

		

		Liferay.Language.available = available;
		Liferay.Language.direction = direction;
	},
	'',
	{
		requires: ['liferay-language']
	}
);