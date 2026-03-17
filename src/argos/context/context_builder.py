def build_context(incident):

    context = {}

    # simulación inicial
    context["environment"] = "prd"
    context["retry_count"] = 0

    incident.context = context

    print(f"[CONTEXT] Built context: {context}")

    return incident