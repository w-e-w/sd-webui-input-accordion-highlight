import gradio as gr
from modules import shared, ui_components


shared.options_templates.update(
    shared.options_section(
        ('ui', 'User interface'),
        {
            'sd_webui_input_accordion_activate_color_light':
                shared.OptionInfo(
                    '#e12885',
                    'InputAccordion highlight - Text color - Light mode', ui_components.FormColorPicker
                ).needs_reload_ui(),
            'sd_webui_input_accordion_activate_shadow_light':
                shared.OptionInfo(
                    '#e12885',
                    'InputAccordion highlight - Border color - Light mode', ui_components.FormColorPicker
                ).needs_reload_ui(),
            'sd_webui_input_accordion_activate_shadow_opacity_light':
                shared.OptionInfo(
                    0.5,
                    'InputAccordion highlight - Border opacity - Light mode', gr.Slider, {"minimum": 0.0, "maximum": 1, "step": 0.01}
                ).needs_reload_ui(),
            'sd_webui_input_accordion_activate_color_dark':
                shared.OptionInfo(
                    '#86cecb',
                    'InputAccordion highlight - Text color - Dark mode', ui_components.FormColorPicker
                ).needs_reload_ui(),
            'sd_webui_input_accordion_activate_shadow_dark':
                shared.OptionInfo(
                    '#86cecb',
                    'InputAccordion highlight - Border color - Dark mode', ui_components.FormColorPicker
                ).needs_reload_ui(),
            'sd_webui_input_accordion_activate_shadow_opacity_dark':
                shared.OptionInfo(
                    0.5,
                    'InputAccordion highlight - Border opacity - Dark mode', gr.Slider, {"minimum": 0.0, "maximum": 1, "step": 0.01}
                ).needs_reload_ui(),
        }
    )
)


shared.gradio_theme.sd_webui_input_accordion_activate_color = shared.opts.sd_webui_input_accordion_activate_color_light
shared.gradio_theme.sd_webui_input_accordion_activate_color_dark = shared.opts.sd_webui_input_accordion_activate_color_dark
shared.gradio_theme.sd_webui_input_accordion_activate_shadow_color = shared.opts.sd_webui_input_accordion_activate_shadow_light + hex(int(shared.opts.sd_webui_input_accordion_activate_shadow_opacity_light * 255))[2:].zfill(2)
shared.gradio_theme.sd_webui_input_accordion_activate_shadow_color_dark = shared.opts.sd_webui_input_accordion_activate_shadow_dark + hex(int(shared.opts.sd_webui_input_accordion_activate_shadow_opacity_dark * 255))[2:].zfill(2)
