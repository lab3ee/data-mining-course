from pathlib import Path

import streamlit as st


st.set_page_config(
	page_title="⛏️ Data Mining",
	page_icon="💎",
	layout="wide"
)


def home_page() -> None:
	st.title("Data Mining")
	st.write(
		"Choose a module tile below to open the corresponding page."
	)

	def render_tile(
		title: str,
		description: str,
		page_path: str,
		image_path: str | None,
		placeholder_text: str,
		notebook_label: str,
		notebook_link: str | None,
		key_prefix: str,
	) -> None:
		with st.container(border=True):
			if image_path and Path(image_path).exists():
				st.image(image_path, width="stretch")
			else:
				st.info(placeholder_text)

			st.markdown(f"**{title}**")

			if st.button(
				"Open page",
				use_container_width=True,
				icon=":material/open_in_new:",
				key=f"{key_prefix}_open_page",
			):
				st.switch_page(page_path)

			if notebook_link:
				st.link_button(
					notebook_label,
					notebook_link,
					use_container_width=True,
					icon=":material/menu_book:",
				)
			else:
				st.button(
					notebook_label,
					disabled=True,
					use_container_width=True,
					icon=":material/disabled_by_default:",
					key=f"{key_prefix}_notebook_disabled",
				)

	tile_cols_row_1 = st.columns(4, gap="small")

	with tile_cols_row_1[0]:
		render_tile(
			title="01: Introduction to Data Mining",
			description="Overview of CRISP-DM phases and foundational concepts for the course.",
			page_path="01_introduction_to_data_mining/module_01_app.py",
			image_path="01_introduction_to_data_mining/images/01_cover.svg",
			placeholder_text="Module preview",
			notebook_label="Notebook NA",
			notebook_link=None,
			key_prefix="module_01",
		)

	with tile_cols_row_1[1]:
		render_tile(
			title="02: Recap Outlier Removal",
			description="Interactive explorer to detect potential outliers using Z-score, IQR, or domain rules.",
			page_path="02_recap_outlier_removal/module_02_app.py",
			image_path="02_recap_outlier_removal/images/02_cover.svg",
			placeholder_text="Module preview",
			notebook_label="Open in Colab",
			notebook_link="https://colab.research.google.com/github/erickoziel/data-mining-course/blob/main/02_recap_outlier_removal/module_02_main.ipynb",
			key_prefix="module_02",
		)

	with tile_cols_row_1[2]:
		render_tile(
			title="03: Transforming Variables",
			description="Explore variable transformations such as normalization, standardization, and power transforms.",
			page_path="03_transforming_variables/module_03_app.py",
			image_path="03_transforming_variables/images/03_cover.svg",
			placeholder_text="Module preview",
			notebook_label="Open in Colab",
			notebook_link="https://colab.research.google.com/github/erickoziel/data-mining-course/blob/main/03_transforming_variables/module_03_main.ipynb",
			key_prefix="module_03",
		)


	with tile_cols_row_1[3]:
		render_tile(
			title="04: Imputation of Missing Values",
			description="Explore techniques for handling missing data, including mean, median, mode imputation, and more advanced methods.",
			page_path="04_imputation_of_missing_values/module_04_app.py",
			image_path="04_imputation_of_missing_values/images/04_cover.svg",
			placeholder_text="Module preview",
			notebook_label="Open in Colab",
			notebook_link="https://colab.research.google.com/github/erickoziel/data-mining-course/blob/main/04_imputation_of_missing_values/module_04_main.ipynb",
			key_prefix="module_04",
		)

	tile_cols_row_2 = st.columns(4, gap="small")

	with tile_cols_row_2[0]:
		render_tile(
			title="05: Balancing Datasets",
			description="Overview of techniques for handling imbalanced datasets, including resampling methods and algorithmic approaches.",
			page_path="05_balancing_and_resampling/module_05_app.py",
			image_path="05_balancing_and_resampling/images/05_cover.svg",
			placeholder_text="Module preview",
			notebook_label="Open in Colab",
			notebook_link="https://colab.research.google.com/github/erickoziel/data-mining-course/blob/main/05_balancing_and_resampling/module_05_main.ipynb",
			key_prefix="module_05",
		)

	with tile_cols_row_2[1]:
		render_tile(
			title="06: Rough Dimensionality Reduction",
			description="Overview of techniques for reducing the dimensionality of datasets, including PCA, LDA, and other methods.",
			page_path="06_rough_dimensionality_reduction/module_06_app.py",
			image_path="06_rough_dimensionality_reduction/images/06_cover.svg",
			placeholder_text="Module preview",
			notebook_label="Open in Colab",
			notebook_link="https://colab.research.google.com/github/erickoziel/data-mining-course/blob/main/06_rough_dimensionality_reduction/module_06_main.ipynb",
			key_prefix="module_06",
		)

	with tile_cols_row_2[2]:
		render_tile(
			title="07: Logistic Regression",
			description="Overview of logistic regression techniques, including model fitting, evaluation, and interpretation.",
			page_path="07_logistic_regression/module_07_app.py",
			image_path="07_logistic_regression/images/07_cover.svg",
			placeholder_text="Module preview",
			notebook_label="Open in Colab",
			notebook_link="https://colab.research.google.com/github/erickoziel/data-mining-course/blob/main/07_logistic_regression/module_07_main.ipynb",
			key_prefix="module_07",
		)

	with tile_cols_row_2[3]:
		render_tile(
			title="08: Feature Reduction, Selection and FA",
			description="Explore techniques for feature reduction, selection, and factor analysis.",
			page_path="08_feature_reduction_selection_and_factor_analysis/module_08_app.py",
			image_path="08_feature_reduction_selection_and_factor_analysis/images/08_cover.svg",
			placeholder_text="Module preview",
			notebook_label="Open in Colab",
			notebook_link="https://colab.research.google.com/github/erickoziel/data-mining-course/blob/main/08_feature_reduction_selection_and_factor_analysis/module_08_main.ipynb",
			key_prefix="module_08",
		)
	
	tile_cols_row_3 = st.columns(4, gap="small")

	with tile_cols_row_3[0]:
		render_tile(
			title="09: Confusion Matrix",
			description="Explore the confusion matrix and its components, including accuracy, precision, recall, and F1 score.",
			page_path="09_confusion_matrix/module_09_app.py",
			image_path="09_confusion_matrix/images/09_cover.svg",
			placeholder_text="Module preview",
			notebook_label="Open in Colab",
			notebook_link="https://colab.research.google.com/github/erickoziel/data-mining-course/blob/main/09_confusion_matrix/module_09_main.ipynb",
			key_prefix="module_09",
		)
	



home = st.Page(home_page, title="Home", icon=":material/home:", default=True)
module_01 = st.Page(
	"01_introduction_to_data_mining/module_01_app.py",
	title="Module 01: Introduction to Data Mining",
)
module_02 = st.Page(
	"02_recap_outlier_removal/module_02_app.py",
	title="Module 02: Recap and Outlier Removal",
)
module_03 = st.Page(
	"03_transforming_variables/module_03_app.py",
	title="Module 03: Transforming Variables",
)
module_04 = st.Page(
	"04_imputation_of_missing_values/module_04_app.py",
	title="Module 04: Imputation of Missing Values",
)

module_05 = st.Page(
	"05_balancing_and_resampling/module_05_app.py",
	title="Module 05: Balancing Datasets",	
)

module_06 = st.Page(
	"06_rough_dimensionality_reduction/module_06_app.py",
	title="Module 06: Rough Dimensionality Reduction",	
)

module_07 = st.Page(
	"07_logistic_regression/module_07_app.py",
	title="Module 07: Logistic Regression",	
)

module_08 = st.Page(
	"08_feature_reduction_selection_and_factor_analysis/module_08_app.py",
	title="Module 08: Feature Reduction, Selection and Factor Analysis",	
)

module_09 = st.Page(
	"09_confusion_matrix/module_09_app.py",
	title="Module 09: Confusion Matrix",	
)

navigation = st.navigation(
	{
		"Course": [home],
		"Modules": [module_01, module_02, module_03, module_04, module_05, module_06, module_07, module_08, module_09],
	}
)

navigation.run()
