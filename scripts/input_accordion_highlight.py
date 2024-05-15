from modules import shared, ui_components


shared.options_templates.update(
    shared.options_section(
        ('ui', 'User interface'),
        {
            'sd_webui_input_accordion_activate_color':
                shared.OptionInfo(
                    '#18ffa8',
                    'Custom InputAccordion enable highlight color', ui_components.FormColorPicker
                ).needs_reload_ui(),
        }
    )
)


shared.gradio_theme.sd_webui_input_accordion_activate_color = shared.opts.sd_webui_input_accordion_activate_color
